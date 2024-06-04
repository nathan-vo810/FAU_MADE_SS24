import urllib.request
import zipfile
import os
import sqlite3
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = {
    "data_dir": "./data",
    "database": "MADE_Project.sqlite",
    "datasets": [
    {
        "url": "https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv",
        "filename": "API_EN.ATM.CO2E.KT_DS2_en_csv_v2",
        "skiprows": 4,
        "skipcols": ["Country Code", "Indicator Name", "Indicator Code"],
        "table_name": "CO2_Emission"
    },
    {
        "url": "https://api.worldbank.org/v2/en/indicator/EG.FEC.RNEW.ZS?downloadformat=csv",
        "filename": "API_EG.FEC.RNEW.ZS_DS2_en_csv_v2",
        "skiprows": 4,
        "skipcols": ["Country Code", "Indicator Name", "Indicator Code"],
        "table_name": "Renewable_Energy_Consumption"
    }],
    "start_year": 1990,
    "end_year": 2020
}

def download_and_extract(url, extract_to):
    try:
        logger.info("Downloading dataset from: %s", url)
        zip_path = os.path.join(extract_to, 'data.zip')
        urllib.request.urlretrieve(url, zip_path)
        logger.info("Downloaded")

        logger.info("Extracting file")
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(path=extract_to)
        logger.info("Extracted")

        os.remove(zip_path)
        logger.info("Removed downloaded ZIP file")

    except Exception as e:
        logger.error("Error downloading or extracting data: %s", e)
        raise


def read_csv_file(data_dir, filename, skiprows):
    try:
        csv_data_file = [f for f in os.listdir(data_dir) if f.startswith(filename)][0]
        logger.info("Reading data from %s", csv_data_file)
        df = pd.read_csv(os.path.join(data_dir, csv_data_file), skiprows=skiprows)
        logger.info("Data read successfully")
        return df
    except Exception as e:
        logger.error("Error reading CSV file: %s", e)
        raise


def transform_data(df, skipcols):
    try:
        # Drop unnecessary columns
        df.drop(skipcols, axis='columns', inplace=True)

        # Remove column with all NaN
        df.dropna(axis=1, how='all', inplace=True)

        # Get year range of the current dataset
        data_year_range = df.columns[4:].to_list()

        # Set year range the same for all dataset (1990 - 2020)
        year_range = [str(year) for year in range(config['start_year'], config['end_year']+1)]
        excluded_year = list(set(data_year_range) - set(year_range))
        df.drop(excluded_year, axis = 1, inplace=True)

        # Drop countries those have NaN values for all years
        df.dropna(subset=year_range, how='all', inplace=True)

        # Fill NaN values with 0
        df.bfill(axis=0, inplace=True)

        logger.info("Data transformation complete")
    except Exception as e:
        logger.error("Error transforming data: %s", e)
        raise


def save_to_sqlite(df, data_dir, db_name, table_name):
    try:
        db_path = os.path.join(data_dir, db_name)
        with sqlite3.connect(db_path) as conn:
            df.to_sql(table_name, con=conn, index=False, if_exists='replace')
        logger.info("Data saved to SQLite database: %s, table: %s", db_name, table_name)
    except Exception as e:
        logger.error("Error saving data to SQLite: %s", e)
        raise


def main():
    datasets = config['datasets']
    data_dir = config['data_dir']
    database = config['database']

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    logger.info("Data directory is set up at: %s", data_dir)

    dfs = []

    for i, dataset in enumerate(datasets):
        logger.info("-" * 30)
        logger.info("Processing Dataset %d", i+1)
        
        try:
            download_and_extract(dataset['url'], data_dir)
            df = read_csv_file(data_dir, dataset['filename'], dataset['skiprows'])
            transform_data(df, dataset['skipcols'])
            dfs.append(df)
        except Exception as e:
            logger.error("Error processing dataset: %s", e)

    countries = set.intersection(*[set(df['Country Name'].values) for df in dfs])

    for i, df in enumerate(dfs):
        df = df[df['Country Name'].isin(countries)]
        save_to_sqlite(df, data_dir, database, datasets[i]['table_name'])


if __name__ == '__main__':
    main()
