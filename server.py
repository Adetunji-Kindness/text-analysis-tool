# Importing flask module in the project is mandatory
# An object of flask class is our WSGI application
from flask import Flask, abort, request
from flask_cors import CORS
from stockAnalyze import getCompanyStockInfo
from analyze import analyzeText
import json

f = open('test/result.json')
stockDataTest = json.load(f)

# Flask constructor takes the name of
# current module (_name_) as arument.
app = Flask(_name_)
CORS(app)

# The route() function of the flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/health', methods=['GET'])
def healthCheck():
    return 'Flask server is up and running'

@app.route('/analyze-stock/<ticker>', methods=['GET'])
def analyzeStock(ticker):
    # return stockDataTest
    if len(ticker) > 5 or not ticker.isidentifier():
        abort(400, 'Invalid ticker symbol')
    try:
        analysis = getCompanyStockInfo(ticker)
    except NameError as e:
        abort(404, e)
    except:
        abort(500, 'Something went wrong running the stock analysis')
    return analysis

@app.route('/analyze-text', methods=['POST'])
def analyzeTextHandler():
    data = request.get_json()
    if 'text' not in data or not data['text']:
        abort(400, 'No text provided to analyze')
    analysis = analyzeText(data['text'])
    return analysis

# main driver function
if _name_ == '_main_':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()