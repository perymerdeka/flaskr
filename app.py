from flask import Flask, render_template, request

app = Flask(__name__)

# route
@app.route("/")
def index():
    query = request.args.get("q")
    if not query:
        return render_template("index.html")
    else:
        return f"query yang dimasukan adalah {query}"


@app.route("/profile/<username>")
def profile(username: str):
    return render_template("profile.html", username=username)
