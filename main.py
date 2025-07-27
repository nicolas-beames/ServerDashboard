from flask import Flask, render_template
from SCRIPT_disk_space import disk_space


app = Flask(__name__)


@app.route("/")
def hello():
    labels = ['Used', 'Available']
    data = []
    for i in disk_space('/'):
        data.append(i)

    return render_template("index.html", labels=labels, data=data)

@app.route("/df")
def disk_files():
    return f"Free Disk Space: {disk_space('/')}"

@app.route("/test")
def test_page():
    labels = ['Used', 'Available']
    data = []
    for i in disk_space('/'):
        data.append(i)
    
    return render_template('test.html', labels=labels, data=data)