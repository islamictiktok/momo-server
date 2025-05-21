from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def run_momo():
    try:
        exec(open("momo_core.py").read(), globals())
        return "✅ momo.py running"
    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
