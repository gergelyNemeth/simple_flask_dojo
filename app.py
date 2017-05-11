from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/request-counter')
def counter():
    return render_template("counter.html")

if __name__ == '__main__':
    app.run(debug=True)
