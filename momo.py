from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def run_momo():
    exec(open("momo_core.py").read())
    return "momo.py running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))