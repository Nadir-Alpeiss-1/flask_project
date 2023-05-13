import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/api/users', methods = ['GET'])
def get_data():
    lst = []
    conn = sqlite3.connect("/Users/zvezdaetogodoma/Desktop/Backend_course_1/april/flask_project/database_for_flask.sqlite3")
    
    cursor = conn.cursor()
    raw_data = cursor.execute("SELECT * FROM users")
    data = raw_data.fetchall()
    keys = list(map(lambda x: x[0], cursor.description))
    for tup in data:
        new_list = [i for i in tup]
        result = dict(zip(keys, new_list))
        lst.append(result)
    return lst

app.run()
