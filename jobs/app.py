from flask import Flask, render_template

# create a Flast instance in the name of app passing a special variable name surrounded by double underscores
app = Flask(__name__)


# create a single route
# in order for this jobs() function to act as a route, we add 2 route decorators 
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')