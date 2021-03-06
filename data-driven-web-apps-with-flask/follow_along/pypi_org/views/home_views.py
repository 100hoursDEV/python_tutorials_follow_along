from pypi_org.infrastructure.view_modifiers import response
import pypi_org.services.package_service as package_service

import flask 

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file='home/index.html')
def index():
    test_packages = package_service.get_latest_packages()
    print(test_packages)
    return {'packages': test_packages}


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {}
