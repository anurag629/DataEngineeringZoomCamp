import argparse

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    csv_url = params.url

    # Download CSV file
    os.system(f"wget {csv_url} -O data.csv")

    # Load data to PostgreSQL
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    df = pd.read_csv('data.csv')
    df.to_sql(name=table_name, con=engine, if_exists='replace')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest data to PostgreSQL')
    parser.add_argument('--user', help='username for PostgreSQL')
    parser.add_argument('--password', help='password for PostgreSQL')
    parser.add_argument('--host', help='host for PostgreSQL')
    parser.add_argument('--port', help='port for PostgreSQL', type=int)
    parser.add_argument('--db', help='database name')
    parser.add_argument('--table_name', help='target table name')
    parser.add_argument('--url', help='URL of the CSV file')
    args = parser.parse_args()

    main(args)