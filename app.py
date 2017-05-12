from flask import Flask, render_template, request, redirect

app = Flask(__name__)

counts = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}


@app.route('/')
@app.route('/request-counter', methods=["GET", "POST"])
def counter():
    global counts
    if request.url.endswith("/request-counter"):
        if request.method == "GET":
            counts["GET"] += 1
        elif request.method == "POST":
            counts["POST"] += 1
        print(counts)
        return redirect('/')
    return render_template("counter.html")


if __name__ == '__main__':
    app.run(debug=True)
