from sqlalchemy import create_engine
import pandas as pd

db_connection_str = 'mysql+pymysql://ferroport_ro:senha@ferroport.managed-otrs.com/otrs'
db_ssl_args = {'ssl_ca': 'C:/OTRS/ferroport-ca-cert.pem',
               'ssl_key': 'C:/OTRS/ferroport-client-key.pem',
               'ssl_cert': 'C:/OTRS/ferroport-client-cert.pem'}
db_connection = create_engine(db_connection_str, connect_args=db_ssl_args)

df = pd.read_sql('SELECT * FROM information_schema.tables', con=db_connection)

print(df)