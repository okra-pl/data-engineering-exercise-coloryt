import json
from flask import Flask, request
from flask_restful import Api
from joblib import load

app = Flask(__name__)
api = Api(app)
model = load('models/lgbr_cars.model')


def shutdown_server():
    """
    Shut down a local flask server
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/predict', methods=['GET'])
def predict() -> dict:
    """
    Add prediction endpoint
    Returns: prediction for instance sent in request
    """
    instance = json.loads(request.data)['instance']
    prediction = model.predict([instance])[0].round(2)

    return {'prediction': prediction}


@app.route('/shutdown', methods=['POST'])
def shutdown():
    """
    Add server shutdown point
    """
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(debug=True)
