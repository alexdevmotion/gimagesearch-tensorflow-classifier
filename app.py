import os

import flask
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from tensorflow_classifier.label_image import classify
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify', methods=['OPTIONS'])
def classify_options():  # temporarily allow unsafe uploads
    resp = flask.Response('Yes you may make unsafe cross-origin requests do this url, kind sir.')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp


@app.route('/classify', methods=['POST'])
def classify_post():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join('upload', filename)
    file.save(filepath)
    result = classify(filepath, model_file='tensorflow_classifier/model/output_graph.pb',
                      label_file='tensorflow_classifier/model/output_labels.txt')
    return flask.jsonify(result)


if __name__ == '__main__':
    app.run()
