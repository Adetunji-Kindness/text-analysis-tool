# Importing flask module in the project is mandatory
# An object of flask class is our WSGI application
from flask import Flask, abort

# Flask constructor takes the name of
# current module (_name_) as arument.
app = Flask(_name_)

# The route() function of the flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/health')
def healthCheck():
    return 'Flask server is up and running'

@app.route('/analyze-stock/<ticker>')
def analyzeStock(ticker):
    if len(ticker) > 5 or not ticker.isidentifier():
        abort(400, 'Invalid ticker symbol')
    return {'data': 'Analysis for' + ticker + 'comming soon'}

# main driver function
if _name_ == '_main_':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()