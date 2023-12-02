from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({
        'msg' : 'I like smartphones',
        'productName' : 'iPhone 14 pro',
        'status' : 200,
        'img' : ''
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)          # 5000 is default port of flask