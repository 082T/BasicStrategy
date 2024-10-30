import numpy as np
import pandas as pd

MAX_LONG_WINDOW = 250


def strategySMA(data: pd.DataFrame, short_window, long_window, price_column="Close"):
    data = data.copy()
    data["short_observations"] = data[price_column].rolling(window=short_window, min_periods=1).mean()
    data["long_observations"] = data[price_column].rolling(window=long_window, min_periods=1).mean()

    data["action"] = 0
    comparison = data["short_observations"][MAX_LONG_WINDOW:] > data["long_observations"][MAX_LONG_WINDOW:]
    actions = np.where(comparison, 1, 0)
    data.loc[data.index[MAX_LONG_WINDOW:], "action"] = actions
    data["action"] = data["action"].shift(1).fillna(0)

    data["daily_return"] = data[price_column].pct_change()
    data["strategy"] = data["action"] * data["daily_return"]

    return (1 + data["strategy"]).cumprod().iloc[-1], data


def strategyEMA(data: pd.DataFrame, short_window=50, long_window=100, price_column="Close"):
    data = data.copy()

    data["short_observations"] = data[price_column].ewm(span=short_window, adjust=False).mean()
    data["long_observations"] = data[price_column].ewm(span=long_window, adjust=False).mean()

    data["action"] = 0
    comparison = data["short_observations"][MAX_LONG_WINDOW:] > data["long_observations"][MAX_LONG_WINDOW:]
    actions = np.where(comparison, 1, 0)
    data.loc[data.index[MAX_LONG_WINDOW:], "action"] = actions
    data["action"] = data["action"].shift(1).fillna(0)

    data["daily_return"] = data[price_column].pct_change()
    data["strategy"] = data["action"] * data["daily_return"]

    return (1 + data["strategy"]).cumprod().iloc[-1], data


strategies = {
    "strategySMA": strategySMA,
    "strategyEMA": strategyEMA,
}
