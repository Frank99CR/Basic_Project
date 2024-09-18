from flask import Flask, request


app = Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello, World!</h1>"



@app.route("/marketplace")
def marketplace():
    return "<h1>Marketplace</h1>"


@app.route("/information", methods=["GET", "POST"])
def information():
	return {
		"year": 2024,
		"description": "Esto es un endpoint secundario",
	}


@app.route("/user/<username>")
def profile(username):
	return f"{username}\'s profile"


@app.route("/shop/<category>/<subcategory>/all")
def products_subcategory(category, subcategory):
    return f"Shopping category {category}, {subcategory}"


if __name__ == "__main__":
    app.run(host="localhost", port=5001,  debug=True)