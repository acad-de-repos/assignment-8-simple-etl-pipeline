# Building a Simple ETL Pipeline Assignment

## Problem Description

In this assignment, you will build a simple Extract, Transform, Load (ETL) pipeline in Python. You will extract data from a CSV file, perform some transformations on it, and then load it into a new table in a SQLite database. This assignment simulates a basic data engineering workflow.

## Learning Objectives

By completing this assignment, you will learn:
- The basic principles of an ETL pipeline
- How to extract data from a source file (CSV)
- How to perform data transformations using pandas
- How to load data into a destination (SQLite database)
- How to orchestrate the ETL steps in a single script

## Setup Instructions

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Make sure you have the following packages installed:
    -   pandas (>=1.3.0)
    -   sqlalchemy (>=1.4.0)

## Instructions

1.  Open the `assignment.py` file.
2.  You will find three function definitions: `extract`, `transform`, and `load`.
3.  Your tasks are to:
    *   **Task 1**: Implement the `extract` function to read data from a CSV file into a pandas DataFrame.
    *   **Task 2**: Implement the `transform` function to perform the following transformations:
        -   Filter out rows where the `age` is less than 18.
        -   Create a new column `full_name` by combining the `first_name` and `last_name` columns.
    *   **Task 3**: Implement the `load` function to load the transformed DataFrame into a SQLite database table named `users`.
4.  Finally, implement the `run_etl` function to orchestrate the entire pipeline by calling the `extract`, `transform`, and `load` functions in the correct order.

## Hints

*   Use `pd.read_csv()` in the `extract` function.
*   In the `transform` function, use boolean indexing to filter the DataFrame and string concatenation to create the `full_name` column.
*   In the `load` function, use `df.to_sql()` to write to the SQLite database. Remember to set the `if_exists` parameter to `'replace'`.

## Testing Your Solution

Run the test file to verify your implementation:

```bash
python test.py
```

The tests will check:

-   That the `extract`, `transform`, and `load` functions work correctly individually
-   That the `run_etl` function successfully orchestrates the pipeline
-   That the final table in the database has the expected data and schema

## Expected Output

The `run_etl` function should create a SQLite database file (if it doesn't exist) and a table named `users` within it, containing the transformed data.

## Sample Data Format

The input CSV file (`data.csv`) will have the following columns:

-   `first_name` (string)
-   `last_name` (string)
-   `age` (integer)
-   `city` (string)

## Troubleshooting

### Common Errors

-   `FileNotFoundError`: Make sure the path to the input CSV file is correct.
-   `DatabaseError`: Check your connection string and the parameters for `to_sql()`.

## Further Exploration (Optional)

*   Add more complex transformations to your pipeline (e.g., handling missing values, standardizing data).
*   How would you add error handling to your ETL pipeline?
*   Explore using a logging framework to log the progress and any errors in your pipeline.
*   Can you modify the pipeline to append data to the table instead of replacing it?

## Resources

-   [What is ETL? A Guide to Extract, Transform, Load](https://www.ibm.com/cloud/learn/etl)
-   [Building a Basic ETL Pipeline with Python](https://www.datacamp.com/community/tutorials/etl-in-python)
-   [Pandas `to_sql` documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
