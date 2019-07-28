from flask import Flask
import json
from flask_mysqldb import MySQL
config = json.load(open('./config.json', 'r'))
app = Flask(__name__)
app.config['MYSQL_HOST'] = config["db"]["MYSQL_HOST"]
app.config['MYSQL_USER'] = config["db"]["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = config["db"]["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = config["db"]["MYSQL_DB"]
mysql = MySQL(app)

app.secret_key = config['secret_key']

from application import routes

cursor = mysql.connection.cursor()
query_string = 'SELECT test FROM new_table'
cursor.execute(query_string)

data = cursor.fetchall()

cursor.close()
print(data)