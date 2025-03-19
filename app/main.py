from flask import Flask
from routes.predict import predict_blueprint

app = Flask(__name__)
app.register_blueprint(predict_blueprint)  # Register the API route

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
