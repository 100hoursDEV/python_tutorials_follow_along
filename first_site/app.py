from flask import Flask, render_template

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from first_site.infrastructure.view_modifiers import response


app = Flask(__name__)


# simulate database:
def get_latest_packages():
    return [
        {"name": "flask", "version": "1.2.3", "description": "jsdfhgdh jfgsdjhfgsdjf gsdjh fgsdhjfgsjfgsj"},
        {"name": "pip", "version": "1.3", "description": "jsdfhgddhjfgsjfgsj"},
        {"name": "reportlab", "version": "4.3", "description": "jsdfhgdh jfgsdjhf gsdjfgsdj hfgsdhjfgsjfgsj"},
        {"name": "flask", "version": "8.32.3", "description": "jsdfhv gdhjfg sdjhfg sdjfgs djhfgsdhjfg sjfgsj"},
        {"name": "Jinja2", "version": "1.3.33", "description": "jsdfhg dhjfgs djhfgsdjfg sdjhfgsdhjf gsjfgsj"},
        {"name": "setuptools", "version": "1.10.93", "description": "jsdfhgdhjfgsdjhfgsdjfgsdjhfgsdhjfgsjfgsj"},
    ]



# @app.route("/")
# def index():
#     test_packages = get_latest_packages()
#     return render_template("home/index.html", packages=test_packages)
#     # seems like the templates folder name is the default for flask so it does not need an explicit path
@app.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)

# @app.route("/about")
# def about():
#     test_packages = get_latest_packages()
#     return render_template("about/about.html")
#     # seems like the templates folder name is the default for flask so it does not need an explicit path
@app.route('/about')
@response(template_file='about/about.html')
def about():
    return {}






if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)