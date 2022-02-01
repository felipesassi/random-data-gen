import pandas as pd
import numpy as np
import random


def generate_create_date_array(
    n_rows: int, first_transaction_date: str, last_transaction_date: str
) -> list:
    """
    Function used to generate random dates from start_date to end_date.

    Parameters
    ----------
    n_rows : int
        Number of rows in dataframe.
    first_transaction_date : str
        First date to generate interval.
    last_transaction_date : str
        Last date to generate interval.

    Returns
    -------
    list
        List of dates.
    """
    created_at_list = list(
        pd.date_range(start=first_transaction_date, end=last_transaction_date, periods=n_rows)
    )
    random.shuffle(created_at_list)

    return created_at_list


def generate_consumer_ids(n_rows: int, n_consumers: int) -> list:
    """
    Function used to generate consumers unique ID's.

    Parameters
    ----------
    n_rows : int
        Number of rows in dataframe.
    n_consumers : int
        Number of unique consumers in dataframe.

    Returns
    -------
    list
        List of consumers.
    """
    consumer_ids = range(1, n_consumers + 1)
    return list(np.random.choice(consumer_ids, n_rows))


def generate_transaction_spend(
    n_rows: int, transaction_mean_value: float, transaction_std_value: float
) -> list:
    """
    Function used to generate consumers spend. The spend is sampled from
    a normal distribution curve.

    Parameters
    ----------
    n_rows : int
        Number of rows in dataframe.
    transaction_mean_value : float
        Mean spend to normal curve creation.
    transaction_std_value : float
        Standard deviation of spend to normal curve creation.

    Returns
    -------
    list
        List of spend.
    """

    return list(np.random.normal(transaction_mean_value, transaction_std_value, n_rows))
