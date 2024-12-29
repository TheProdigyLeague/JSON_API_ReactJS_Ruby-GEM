# $ pip install flask-cors
# $ pip show flask-cors
# $ pip install flask-swagger-ui
from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask import jsonify, request # assume swagger JSON file SWAGGER_URL = '/api/docs' 

app = Flask(__name__)
CORS(app) # API_URL = '/static/swagger.json' exposed Swagger.json

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': 'webullsdk'})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/hello', methods=['GET', 'POST', 'PUT'])
def index():
    if request.method == 'POST':
        data = request.json
    elif request.method == 'PUT':
        data = request.json
    else:
        data = {"webull": "sdkcores"}

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
# http://127.0.0.1:5000
