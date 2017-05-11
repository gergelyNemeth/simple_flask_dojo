from flask import Flask

app = Flask(__name__)


@app.route('/request-counter')
def counter():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)
