from flask import Flask, render_template, request, session

app = Flask(__name__)

app.secret_key = "This Secret Key"

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


@app.route("/set_email", methods=["GET", "POST"])
def set_email():
    if request.method == "POST":
        # save session
        session["email"] = request.form["email_address"]
    return render_template("set_email.html")


# get session email
@app.route("/get_email")
def get_email():
    return render_template("get_email.html")


# delete session email
@app.route("/delete_email")
def delete_email():
    # Clear the email stored in the session object
    session.pop("email", default=None)
    return "<h1>Session deleted!</h1>"
