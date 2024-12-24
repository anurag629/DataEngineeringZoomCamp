import pandas as pd
import argparse
from time import time
from sqlalchemy import create_engine


def main():
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    
    # Adjust the connection string for both Windows and Ubuntu
    # engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # df_iter = pd.read_csv("yellow_tripdata_2021-01.csv", iterator=True, chunksize=1000)
    df_iter = pd.read_csv(url, iterator=True, chunksize=1000)


    df = next(df_iter)

    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)

    # df.head(n=0).to_sql('yellow_taxi_data', engine, if_exists='replace', index=False)
    df.head(n=0).to_sql(table_name, engine, if_exists='replace', index=False)
    
    # df.to_sql('yellow_taxi_data', engine, if_exists='append', index=False)
    df.to_sql(table_name, engine, if_exists='append', index=False)



    # while True:
    #     try:
    #         t_start = time()
    #         df = next(df_iter)
    #         df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            
    #         # df.to_sql('yellow_taxi_data', engine, if_exists='append', index=False)
    #         df.to_sql(table_name, engine, if_exists='append', index=False)
    #         t_end = time()
    #         print(f"Chunk loaded in {t_end - t_start} seconds")
    #     except StopIteration:
    #         break
        
    # print("All data loaded")
    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data into PostgreSQL')


    # user, password, host, port, and database are the arguments, database name, table name, url of the csv file

    parser.add_argument('--user', type=str, help='PostgreSQL username')
    parser.add_argument('--password', type=str, help='PostgreSQL password')
    parser.add_argument('--host', type=str, help='PostgreSQL host')
    parser.add_argument('--port', type=str, help='PostgreSQL port')
    parser.add_argument('--db', type=str, help='PostgreSQL database name')
    parser.add_argument('--table-name', type=str, help='PostgreSQL table name')
    parser.add_argument('--url', type=str, help='URL of the CSV file')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
    main(args)

