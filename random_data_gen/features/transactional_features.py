import pandas as pd
import numpy as np


def generate_create_date_array(n_rows: int, start_date: str, end_date: str) -> list:
    """
    Function used to generate random dates from start_date to end_date.

    Parameters
    ----------
    n_rows : int
        Number of rows in dataframe.
    start_date : str
        First date to generate interval.
    end_date : str
        Last date to generate interval.

    Returns
    -------
    list
        List of dates.
    """
    return list(pd.date_range(start=start_date, end=end_date, periods=n_rows))


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
    n_rows: int, mean_spend: float, std_spend: float
) -> list:
    """
    Function used to generate consumers spend. The spend is sampled from
    a normal distribution curve.

    Parameters
    ----------
    n_rows : int
        Number of rows in dataframe.
    mean_spend : float
        Mean spend to normal curve creation.
    std_spend : float
        Standard deviation of spend to normal curve creation.

    Returns
    -------
    list
        List of spend.
    """

    return list(np.random.normal(mean_spend, std_spend, n_rows))
