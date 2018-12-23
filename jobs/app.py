# import global helper g from Flask
from flask import Flask, render_template, g
import sqlite3

PATH = 'db/jobs.sqlite'

# create a Flast instance in the name of app passing a special variable name surrounded by double underscores
app = Flask(__name__)


def open_connection():
    connection = getattr(g, '_connection', None)

    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    
    if (commit is True):
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()


# create a single route
# in order for this jobs() function to act as a route, we add 2 route decorators 
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')