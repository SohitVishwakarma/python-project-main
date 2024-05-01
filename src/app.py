from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello This is testing For auto deployment !"


if __name__ == "__main__":
    app.run()

