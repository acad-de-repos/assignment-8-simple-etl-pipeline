import unittest
import pandas as pd
import os
from sqlalchemy import create_engine, inspect
from assignment import extract, transform, load, run_etl

class TestETLPipeline(unittest.TestCase):
    def setUp(self):
        """Set up temporary data and database files for testing"""
        self.csv_file = 'test_data.csv'
        self.db_file = 'test_db.sqlite'
        self.table_name = 'users'

        data = {
            'first_name': ['John', 'Jane', 'Peter', 'Sue'],
            'last_name': ['Doe', 'Doe', 'Jones', 'Smith'],
            'age': [25, 17, 35, 42],
            'city': ['New York', 'London', 'Paris', 'Tokyo']
        }
        pd.DataFrame(data).to_csv(self.csv_file, index=False)

    def tearDown(self):
        """Clean up created files after each test"""
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.db_file):
            os.remove(self.db_file)
        # Dispose of the engine created in setUp if it exists
        if hasattr(self, 'engine'):
            self.engine.dispose()

    def test_extract(self):
        """Test the extract function"""
        df = extract(self.csv_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape[0], 4)

    def test_transform(self):
        """Test the transform function"""
        df = extract(self.csv_file)
        transformed_df = transform(df)
        self.assertEqual(transformed_df.shape[0], 3)
        self.assertIn('full_name', transformed_df.columns)

    def test_load(self):
        """Test the load function"""
        engine = create_engine(f'sqlite:///{self.db_file}')
        with engine.connect() as connection:
            df = extract(self.csv_file)
            transformed_df = transform(df)
            load(transformed_df, connection, self.table_name)

            inspector = inspect(engine)
            self.assertTrue(inspector.has_table(self.table_name))

    def test_run_etl(self):
        """Test the end-to-end ETL pipeline"""
        run_etl(self.csv_file, self.db_file, self.table_name)
        engine = create_engine(f'sqlite:///{self.db_file}')
        with engine.connect() as connection:
            df = pd.read_sql_table(self.table_name, connection)
            self.assertEqual(df.shape[0], 3)
            self.assertIn('full_name', df.columns)

if __name__ == '__main__':
    unittest.main()
