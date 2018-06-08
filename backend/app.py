from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/classify')
def classify():
    return 'Classified!'


if __name__ == '__main__':
    app.run()
