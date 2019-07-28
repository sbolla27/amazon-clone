from amazon_clone import app, mysql

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    query_string = 'SELECT test FROM new_table'
    cursor.execute(query_string)

    data = cursor.fetchall()

    cursor.close()
    return data