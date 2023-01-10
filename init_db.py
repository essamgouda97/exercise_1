import sqlite3
import pandas as pd

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''CREATE TABLE users (id int, first_name text, last_name text, email text, gender text, ip_address text, salary int, country text)''')

# load the data into a Pandas DataFrame
users = pd.read_csv('db.csv')
# write the data to a sqlite table
users.to_sql('users', conn, if_exists='append', index = False)
