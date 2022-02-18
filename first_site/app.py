from flask import Flask, render_template

app = Flask(__name__)


# simulate database:
def get_latest_packages():
    return [
        {"name": "flask", "version": "1.2.3", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
        {"name": "pip", "version": "1.3", "description": "jsdfhgddhjfgsjfgsj"},
        {"name": "reportlab", "version": "4.3", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
        {"name": "flask", "version": "8.32.3", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
        {"name": "Jinja2", "version": "1.3.33", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
        {"name": "setuptools", "version": "1.10.93", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
    ]



@app.route("/")
def index():
    test_packages = get_latest_packages()
    return render_template("index.html", packages=test_packages)
    # seems like the templates folder name is the default for flask so it does not need an explicit path

if __name__ == "__main__":
    app.run(debug=True)