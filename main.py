from flask import Flask, render_template
from SCRIPT_disk_space import disk_space

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", df=disk_space('/'))


@app.route("/df")
def disk_files():
    return f"Free Disk Space: {disk_space('/')}"

@app.route("/test")
def test_page():
    return "test"