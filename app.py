from datetime import datetime
import logging
import logging.config
import yaml
import traceback
from time import strftime
from flask import Flask, json, jsonify, make_response, request
from flask.json.provider import DefaultJSONProvider 
#JSONEncoder = DefaultJSONProvider().encoder
from flasgger import Swagger
from werkzeug.exceptions import HTTPException
from api.model.error import ErrorModel
from api.resources.errors import ApiError
from api.route.version import version_api
from api.route.profile import investment_simulation_api
from api.schema.error import ErrorSchema
from init import load_config


def create_app():

    logging.config.dictConfig(yaml.safe_load(open("logging_config.yml").read()))

    app = Flask(__name__)
    
    JSONEncoder = DefaultJSONProvider().encoder
    app.json = DefaultJSONProvider(app)
    
    
    app.config['SWAGGER'] = {
        'title': 'Flask API Colf-pv-investment-simulation-core',
    }

    Swagger(app)

    ## Initialize Config
    config = load_config()
    logging.info("MODE: " + config.MODE)
    app.config.from_object(config)
    app.register_blueprint(version_api, url_prefix='/simulator-core/api/v1')
    app.register_blueprint(investment_simulation_api, url_prefix='/simulator-core/api/v1')

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""

        error = ErrorModel()
        error.code = e.code 
        error.description = e.name + ": " + e.description
        error.path = request.path 
        error.timestamp = datetime.now()
        response = make_response(jsonify({"content": None, "error": ErrorSchema().dump(error) }), 200)
        response.headers["Content-Type"] = "application/json"

        tb = traceback.format_exc()
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logging.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
        return response 

    @app.errorhandler( ApiError )
    def handle_custom_exception(e):
        return e.response()

    @app.after_request
    def after_request(response):
        timestamp = strftime('[%Y-%b-%d %H:%M]')
        logging.info('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
        return response

    return app



if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()
    app.run(host='0.0.0.0', port=port)



