from flask import Flask, jsonify
import readfromexcel

app = Flask(__name__)


@app.route('/')
def index():
    return "Home page!"


@app.route('/movies')
def get_movies():
    return jsonify(readfromexcel.readmovies('data/movies.csv'))


@app.route('/ratings')
def get_ratings():
    return jsonify(readfromexcel.readratings('data/ratings.csv'))


@app.route('/links')
def get_links():
    return jsonify(readfromexcel.readlinks('data/links.csv'))


@app.route('/tags')
def get_tags():
    return jsonify(readfromexcel.readtags('data/tags.csv'))


if __name__ == '__main__':
    app.run()

