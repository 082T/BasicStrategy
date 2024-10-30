import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from typing import Any


def analyze_results(strategy_return: float,
                    data: pd.DataFrame,
                    short_window_length: int,
                    long_window_length: int,
                    strategy: Any,
                    risk_free_rate: float = 0.0):
    data["equity_curve"] = (1 + data["strategy"]).cumprod()
    data["peak"] = data["equity_curve"].cummax()
    data["drawdown"] = (data["equity_curve"] - data["peak"]) / data["peak"]
    max_drawdown = data["drawdown"].min()

    data["excess_return"] = data["strategy"] - (risk_free_rate / 252)
    sharpe_ratio = (data["excess_return"].mean() * np.sqrt(252) / data["excess_return"].std())

    start_index = data[data["action"] == 1].index[0]
    data["benchmark"] = (1 + data["daily_return"][start_index:]).cumprod()
    data["benchmark"].fillna(1)

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    data["equity_curve"].plot(ax=axes[0], label="Strategy equity curve", color="blue")
    data["benchmark"].plot(ax=axes[0], label="Benchmark daily return", color="red")
    axes[0].set_title("Equity curve vs Benchmark")
    axes[0].set_ylabel("Equity")
    axes[0].legend()

    data["drawdown"].plot(ax=axes[1], title="Drawdown", color="red")
    axes[1].set_ylabel("Drawdown")

    plt.tight_layout()
    plt.savefig("plots/analysis.png")

    print(f"Final Cumulative Return: {strategy_return:.2%}")
    print(f"Max Drawdown: {max_drawdown:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Strategy: {strategy.__name__}, with windows: {short_window_length}/{long_window_length}")
