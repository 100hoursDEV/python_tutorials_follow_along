from flask import Flask, render_template

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import package_service
app = Flask(__name__)


def main():
    register_blueprints()
    app.run(debug=True, use_reloader=True)


def register_blueprints():
    from pypi_org.views import home_views
    from pypi_org.views import package_views
    # from pypi_org.views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)


if __name__ == "__main__":
    main()
