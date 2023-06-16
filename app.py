from flask import Flask, request, jsonify, Response
from flask_swagger_ui import get_swaggerui_blueprint
from controllers.movies import get_movies, get_by_id, insert_movie, update_movie_by_id
from db import create_tables


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
        print(type(movie))
        if not movie.get('title') or not movie.get('release_year'):
            return Response("Bad request: missing argument", status=400)
        if movie.get('description') is None:
            movie['description'] = ''
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
        if not movie.get('title') or not movie.get('release_year'):
            return Response("Bad request: missing argument", status=400)
        if movie.get('description') is None:
            movie['description'] = ''

        updated_movie = update_movie_by_id(movie, id)
        if not updated_movie:
            return Response("id not found", status=404)
        return jsonify(updated_movie)


if __name__ == '__main__':
    create_tables()
    app.run(port=8000)
