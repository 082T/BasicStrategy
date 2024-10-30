import argparse
import optimization

from data import DataLoader
from datetime import datetime
from analysis import analyze_results
from strategy import strategies


def get_argument_parser():
    parser = argparse.ArgumentParser("SMA Crossover")
    parser.add_argument("--ticker",
                        type=str,
                        default="SPY",
                        help="Ticker symbol")
    parser.add_argument("--start_date",
                        type=lambda date: datetime.strptime(date, "%d-%m-%Y"),
                        default=datetime.strptime("01-01-2010", "%d-%m-%Y"),
                        help="Backtesting start date")
    parser.add_argument("--end_date",
                        type=lambda date: datetime.strptime(date, "%d-%m-%Y"),
                        default=datetime.strptime("01-01-2024", "%d-%m-%Y"),
                        help="Backtesting end date")
    parser.add_argument("--short_window", type=int, default=5, help="SMA short window length")
    parser.add_argument("--long_window", type=int, default=50, help="SMA long window length")
    parser.add_argument("--optimize", action="store_true", help="Optimize SMA parameters")
    parser.add_argument("--strategy", type=str, default="strategySMA", help="Strategy to test")

    return parser.parse_args()


def main():
    args = get_argument_parser()
    data_loader = DataLoader(args.ticker)
    ticker_data = data_loader.grab(start=args.start_date,
                                   end=args.end_date,
                                   interval="1d",
                                   data_type="Close")
    strategy = strategies[args.strategy]
    if args.optimize:
        optimized_values = optimization.optimize_params(ticker_data, strategy=strategy)
        short_window_for_eval = int(optimized_values["short_window"])
        long_window_for_eval = int(optimized_values["long_window"])
    else:
        short_window_for_eval = args.short_window
        long_window_for_eval = args.long_window

    result, data = strategy(ticker_data, short_window_for_eval, long_window_for_eval)
    analyze_results(result, data, short_window_for_eval, long_window_for_eval, strategy)


if __name__ == "__main__":
    main()
