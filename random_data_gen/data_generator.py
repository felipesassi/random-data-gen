import pandas as pd
from random_data_gen.features.transactional_features import (
    generate_create_date_array,
    generate_consumer_ids,
    generate_transaction_spend,
)


class TransactionalDataGenerator:
    def __init__(
        self,
        n_rows: int,
        n_consumers: int,
        transaction_mean_value: float,
        transaction_std_value: float,
        first_transaction_date: str,
        last_transaction_date: str,
    ) -> None:

        self.n_rows = n_rows
        self.n_consumers = n_consumers
        self.transaction_mean_value = transaction_mean_value
        self.transaction_std_value = transaction_std_value
        self.first_transaction_date = first_transaction_date
        self.last_transaction_date = last_transaction_date

    def __call__(self):

        transaction_created_at_list = generate_create_date_array(
            self.n_rows, self.first_transaction_date, self.last_transaction_date
        )
        transaction_consumer_id_list = generate_consumer_ids(self.n_rows, self.n_consumers)
        transaction_spend_list = generate_transaction_spend(
            self.n_rows, self.transaction_mean_value, self.transaction_std_value
        )

        return pd.DataFrame(
            data={
                "consumer_id": transaction_consumer_id_list,
                "transaction_created_at": transaction_created_at_list,
                "transaction_payment_value": transaction_spend_list,
            }
        )
