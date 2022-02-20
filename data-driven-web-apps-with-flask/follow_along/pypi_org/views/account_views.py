from pypi_org.infrastructure.view_modifiers import response

import flask

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


# ########  INDEX  ############
@blueprint.route('/account')
def index():
    return f"home page for accounts"


# ########  REGISTER  ############
@blueprint.route('/account/register', methods=["GET"])
# @response(template_file='packages/details.html')
def register_get():
    return f"Register page"


@blueprint.route('/account/register', methods=["POST"])
# @response(template_file='packages/details.html')
def register_post():
    return f"Register page"


# ########  LOGIN  ############
@blueprint.route('/account/login', methods=["GET"])
# @response(template_file='packages/details.html')
def login_get():
    return f"Login page"


@blueprint.route('/account/login', methods=["POST"])
# @response(template_file='packages/details.html')
def login_post():
    return f"Login page"


# ########  LOGOUT  ############
@blueprint.route('/account/logout', methods=["GET"])
# @response(template_file='packages/details.html')
def logout():
    return f"Logout page"
