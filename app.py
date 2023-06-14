from flask import Flask, request, jsonify, Response
from controllers.movies import *
from db import create_tables

app = Flask(__name__)

@app.route('/movies', methods=['GET', 'POST'])
def create_movie():
    if request.method == 'GET':
        return jsonify(get_movies())

@app.route('/movies/<int:id>',  methods=['GET', 'PUT'])
def update_movie(id):
    if request.method == 'GET':
        movie = get_by_id(id)
        if not movie:
            return Response("id not found", status=404)
        return jsonify(movie)

if __name__ == '__main__':
    create_tables()
    app.run(port=8000)