# Random Data Generator

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>



This is a test package to generate random transactional data. 

With this package you can create a table with transactional data containing:

- consumer_id: ID identifing the customer that does the transaction;
- created_at: Date of transaction;
- payment_value: Monetary value of transaction.

All this fields are customizable.

## How to use

You can start the use o RandomDataGen with this example code:

``` python
from random_data_gen.data_generator import DataGenerator

TRGenerator = DataGenerator(
    n_rows=1000,
    n_ids=100,
    mean_spend=100,
    std_spend=10,
    start_date="2020-01-01",
    end_date="2021-01-01",
)

df = TRGenerator()
```

In this snippet we defined a table with 1000 rows, 100 unique users, a mean spend in transactions of 100 u.m. a standard deviation in transactional spend of 10u.m., the start date (2020-01-01) and the end date (2021-01-01).

The *df* returned is in the form:

```
| consumer_id | created_at                    | payment_value |
|-------------|-------------------------------|---------------|
| 234         | 2020-02-03 02:15:12.051981122 | 120.10        |
| 43          | 2020-05-11 08:47:34.054054054 | 87.10         |
| 3123        | 2020-12-30 21:37:17.837837840 | 12.84         |
```