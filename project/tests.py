import unittest

import os
import pandas as pd
import numpy as np
import sqlite3

from data_ETL import download_and_extract, read_csv_file, transform_data, save_to_sqlite, config


class TestETLPipeline(unittest.TestCase):
    def setUp(self) -> None:
        self.data_dir = "./test_data"
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.db_path = os.path.join(self.data_dir, "test_database.sqlite")
        self.test_csv = os.path.join(self.data_dir, "test_data.csv")
        self.mock_csv_content = """"Data Source","World Development Indicators",

"Last Updated Date","2024-05-30",
        
"Country Name","Country Code","Indicator Name","1989","1990","1991","1992"
"Germany","DE","CO2","","900","880","850"
"United States","US","CO2","","","600","700"
"France","FR","CO2","","","","30"
"Italy","IT","CO2","","","",""
"""
        with open(self.test_csv, "w") as f:
            f.write(self.mock_csv_content)

        self.mock_df = pd.DataFrame({
            "Country Name": ["Germany", "United States", "France", "Italy"],
            "Country Code": ["DE", "US", "FR", "IT"],
            "Indicator Name": ["CO2", "CO2", "CO2", "CO2"],
            "1989": [np.nan, np.nan, np.nan, np.nan],
            "1990": [900, np.nan, np.nan, np.nan],
            "1991": [880, 600, np.nan, np.nan],
            "1992": [850, 700, 30, np.nan]
        })

    def tearDown(self) -> None:
        if os.path.exists(self.data_dir):
            for file in os.listdir(self.data_dir):
                os.remove(os.path.join(self.data_dir, file))
            os.rmdir(self.data_dir)

    def test_download_and_extract(self):
        for i, dataset in enumerate(config["datasets"]):
            download_and_extract(dataset["url"], self.data_dir)

            # Check if files are extracted (3 files/zip)
            self.assertTrue(len(os.listdir(self.data_dir)) - 1 == 3*(i+1))

            # Check if zip file is removed        
            self.assertFalse(os.path.exists(os.path.join(self.data_dir, "data.zip")))

    def test_read_csv(self):
        df = read_csv_file(self.data_dir, "test_data.csv", 4)
        pd.testing.assert_frame_equal(df, self.mock_df)

    def test_transform(self):
        transformed_df = self.mock_df.copy()
        
        skipcols=["Country Code", "Indicator Name"]
        year_range = ["1990", "1991", "1992"]

        transformed_df = transform_data(transformed_df, skipcols, year_range)

        # Test shape
        self.assertEqual(transformed_df.shape, (3,4))

        # Test columns
        self.assertEqual(transformed_df.columns.to_list(), ["Country Name", "1990", "1991", "1992"])

        # Test fill nan value
        self.assertEqual(transformed_df["1990"][1], 600)
        self.assertEqual(transformed_df["1990"][2], 30)
        self.assertEqual(transformed_df["1991"][2], 30)

    def test_save_to_sqlite(self):
        save_to_sqlite(self.mock_df, self.data_dir, "test_database.sqlite", "test_table")

        # Check if db is saved
        self.assertTrue(os.path.exists(self.db_path))
        
        with sqlite3.connect(self.db_path) as conn:
            result_df = pd.read_sql_query("SELECT * FROM test_table", conn,
                                          dtype={'1989': np.float64})
            pd.testing.assert_frame_equal(result_df, self.mock_df)

    def test_system(self):
        from data_ETL import main
        main()

        datasets = config["datasets"]
        db_path = os.path.join(config["data_dir"], config["database"])

        # Check if database exists
        self.assertTrue(os.path.exists(db_path))

        for dataset in datasets:
            with sqlite3.connect(db_path) as conn:
                result_df = pd.read_sql_query(f"SELECT * FROM {dataset['table_name']}", conn)

                # Check shape
                self.assertEqual(result_df.shape, (239, 32))

                # Check if all nan values are filled
                self.assertFalse(result_df.isnull().values.any())

                # Check columns
                years_range = [str(year) for year in range(1990, 2021)]
                self.assertEqual(result_df.columns.to_list(), ["Country Name", *years_range])


if __name__ == "__main__":
    unittest.main()
