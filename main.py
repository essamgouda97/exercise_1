from flask import Flask
import sqlite3
import json

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/users', methods=['GET'])
def index():
    """
    Get all users from the database
    """
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    
    return json.dumps([tuple(row) for row in users])

## Write your code here

if __name__ == '__main__':
   app.run(debug = True)