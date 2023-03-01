from flask import Flask,jsonify, request
from flask_restful import Resource, Api, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)
data=pd.read_csv("/home/aashish/Desktop/StreamData/Sample-Spreadsheet-10-rows.csv",encoding='unicode_escape')
df2 = data.to_dict('records')
print(df2)
@app.route('/')
def emp_details():
    return jsonify(df2)


if __name__ == '__main__':
    app.run()
