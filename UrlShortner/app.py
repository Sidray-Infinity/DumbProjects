from flask import Flask

def setupRoutes(app: Flask):
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app = Flask(__name__)
    setupRoutes(app)
    app.run(debug=True)