from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counts = 0


@app.route('/')
@app.route('/request-counter', methods=["GET", "POST"])
def counter():
    global counts
    if request.url.endswith("/request-counter"):
        counts += 1
        print(counts)
        return redirect('/')
    return render_template("counter.html")


if __name__ == '__main__':
    app.run(debug=True)
