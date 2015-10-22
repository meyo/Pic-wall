from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "hello"
	pass

if __name__ == '__main__':
	app.run(debug=True)