from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def read_request_counts():
    with open("request_counts.txt") as f:
        request_counts_data = f.readlines()
        request_counts = []
        for request_count in request_counts_data:
            method, count = request_count.split(": ")
            request_counts.append([method, int(count)])
        return request_counts


def write_request_counts(method):
    counts = read_request_counts()
    for count in counts:
        if count[0] == method:
            count[1] += 1
    with open("request_counts.txt", "w") as f:
        for count in counts:
            f.write(": ".join([count[0], str(count[1])]) + "\n")


@app.route('/')
@app.route('/request-counter', methods=["GET", "POST", "DELETE", "PUT"])
def counter():
    if request.url.endswith("/request-counter"):
        write_request_counts(request.method)
        return redirect('/')
    return render_template("counter.html")


if __name__ == '__main__':
    app.run(debug=True)
