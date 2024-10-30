import hyperopt


def optimize_params(ticker_data, strategy, price_column="Close"):
    def objective(params):
        short_window = int(params["short_window"])
        long_window = int(params["long_window"])

        performance, _ = strategy(ticker_data, short_window, long_window, price_column)
        return -performance

    search_space = {
        "short_window": hyperopt.hp.quniform("short_window", 1, 50, 1),
        "long_window": hyperopt.hp.quniform("long_window", 50, 250, 1)
    }
    return hyperopt.fmin(fn=objective, space=search_space, algo=hyperopt.tpe.suggest, max_evals=500)
