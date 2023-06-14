from flask import Flask, request, jsonify, Response
from db import create_tables

app = Flask(__name__)

@app.route('/movies', methods=['GET', 'POST'])
def create_movie():
    pass

@app.route('/movies/<int:id>',  methods=['GET', 'PUT'])
def update_movie(id):
    pass

if __name__ == '__main__':
    create_tables()
    app.run(port=8000)