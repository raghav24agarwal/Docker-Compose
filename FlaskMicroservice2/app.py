from flask import Flask, render_template
from consume import consume_data

app = Flask(__name__)

@app.route('/productpage', methods=['GET'])
def index():
    microservice1data = consume_data()
    return render_template('index.html', context=microservice1data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)  