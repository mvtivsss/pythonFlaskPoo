from flask import Flask, jsonify
from regions import regions

app = Flask(__name__)

@app.route('/regions')
def getRegions():
    return jsonify({'regiones': regions})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)