from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello mukul this is our Azure App Service!"

if __name__ == "__main__":
    app.run()
