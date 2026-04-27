from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "Hello Eugeniu, This is your first app deployed in container"

app.run(host="0.0.0.0", port=5000)
