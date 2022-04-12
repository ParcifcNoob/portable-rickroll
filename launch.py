# Copyright 2022 iiPython

# Modules
from flask_compress import Compress
from flask import Flask, render_template

# Initialization
app = Flask("Rickroll")
Compress(app)

# Routes
@app.route("/")
def index() -> None:
    return render_template("index.html"), 200

# Launch
if __name__ == "__main__":
    app.run(
        host = "0.0.0.0",
        port = 8080,
        debug = True
    )
