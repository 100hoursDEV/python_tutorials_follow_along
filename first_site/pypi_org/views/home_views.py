from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service
import flask 

blueprint = flask.Blueprint('home', __name__, template_folder='templates')

# @app.route("/")
# def index():
#     test_packages = get_latest_packages()
#     return render_template("home/index.html", packages=test_packages)
#     # seems like the templates folder name is the default for flask so it does not need an explicit path
@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    return {'packages': test_packages}
    # return flask.render_template('home/index.html', packages=test_packages)


# @app.route("/about")
# def about():
#     test_packages = get_latest_packages()
#     return render_template("about/about.html")
#     # seems like the templates folder name is the default for flask so it does not need an explicit path
@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
