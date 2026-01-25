# Importing flask module in the project is mandatory
# An object of flask class is our WSGI application
from flask import flask

# Flask constructor takes the name of
# current module (_name_) as arument.
app = Flask(_name_)

# The route() function of the flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/health')
def hello_world():
    return 'Flask server is up and running'

# main driver function
if _name_ == '_main_':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()