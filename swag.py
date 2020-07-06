#!flask/bin/python
from flask import Flask
from flask import jsonify, request
from flask_cors import CORS

from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
CORS(app)

### swagger specific ###
swagger_url = '/doc'
api_url = '/static/swagger.json'
ui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "test"
    }
)
app.register_blueprint(ui_blueprint, url_prefix=swagger_url)


@app.route('/hello', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        data = request.json
    elif request.method == 'PUT':
        data = request.json
    else:
        data = {"hello": "world!"}

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
