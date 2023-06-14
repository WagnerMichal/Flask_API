from flask import Flask, request, jsonify, Response
from controllers.movies import *
from db import create_tables
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tietoevry-API"
    },
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/movies', methods=['GET', 'POST'])
def create_movie():
    if request.method == 'GET':
        return jsonify(get_movies())

    if request.method == 'POST':
        movie = request.get_json()
        if not movie['title'] or not movie['release_year']:
            return Response("Bad request", status=400)
        return jsonify(insert_movie(movie))


@app.route('/movies/<int:id>',  methods=['GET', 'PUT'])
def update_movie(id):
    if request.method == 'GET':
        movie = get_by_id(id)
        if not movie:
            return Response("id not found", status=404)
        return jsonify(movie)

    if request.method == 'PUT':
        movie = request.get_json()
        updated_movie = update_movie_by_id(movie, id)

        if not updated_movie:
            return Response("id not found", status=404)
        return jsonify(updated_movie)


if __name__ == '__main__':
    create_tables()
    app.run(port=8000)
