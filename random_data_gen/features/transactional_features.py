import pandas as pd
import numpy as np


def generate_create_date_array(n_rows: int, start_date: str, end_date: str) -> list:
   
    return list(pd.date_range(start=start_date, end=end_date, periods=n_rows))


def generate_consumer_ids(n_rows: int, n_ids: int) -> list:

    consumer_ids = range(1, n_ids + 1)
    return list(np.random.choice(consumer_ids, n_rows))


def generate_transaction_spend(
    n_rows: int, mean_spend: float, std_spend: float
) -> list:

    return list(np.random.normal(mean_spend, std_spend, n_rows))
