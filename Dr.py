from flask import Flask, request
from random import choice, seed
import pandas as pd
from pandas import read_csv

df = pd.read_csv("name.csv")
names = df.Name.tolist()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def num():
    num = request.args.get("number")
    seed(num)
    hey = choice(names)
    return hey

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)
