import pandas as pd
from random_data_gen.features.transactional_features import (
    generate_create_date_array,
    generate_consumer_ids,
    generate_transaction_spend,
)


class DataGenerator:
    def __init__(
        self,
        n_rows: int,
        n_consumers: int,
        mean_spend: float,
        std_spend: float,
        start_date: str,
        end_date: str,
    ) -> None:

        self.n_rows = n_rows
        self.n_consumers = n_consumers
        self.mean_spend = mean_spend
        self.std_spend = std_spend
        self.start_date = start_date
        self.end_date = end_date

    def __call__(self):

        date_list = generate_create_date_array(
            self.n_rows, self.start_date, self.end_date
        )
        consumer_list = generate_consumer_ids(self.n_rows, self.n_consumers)
        transactional_spend_list = generate_transaction_spend(
            self.n_rows, self.mean_spend, self.std_spend
        )

        return pd.DataFrame(
            data={
                "consumer_id": consumer_list,
                "created_at": date_list,
                "payment_value": transactional_spend_list,
            }
        )
