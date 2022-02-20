from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service
import flask 

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')


@blueprint.route('/project/<package_name>')
@response(template_file='packages/details.html')
def package_details(package_name):
    return f"Package details for {package_name}"