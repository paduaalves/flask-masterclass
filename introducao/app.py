from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "<a href='/posts'>Posts</a>"


@app.route("/posts")
@app.route("/posts/<int:id>")
def posts(id):
    data = dict(
        patth=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=request.args.get("titulo"),
        id=id if id else 0

    )
    return data


if __name__ == "__main__":
    app.run()
