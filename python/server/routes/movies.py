"""Movies routes"""
from flask import request, jsonify  # distinguish types of requests
import json
from server.model.movies import list_all, get_by_id
from server.controller.model_control import add_new_movie
from common.tools import match_values_to_column_sequence, get_todays_date_iso_format


def serve(app):
    @app.route('/movies', methods=['GET', 'POST'])
    def get_all_movies():
        print(f'{request.method} request performed.')

        if request.method == 'GET':
            results = list_all()
            return jsonify(
                data=results,
                message='all movies',
                statusCode=200,
                method='GET/LIST'
            )

        if request.method == 'POST':
            req_body = json.loads(request.data)
            if req_body['runtime']:
                req_body['runtime'] = json.dumps(req_body['runtime'])

            results = add_new_movie(req_body)
            if len(results):
                message = f'Found {len(results)} results.'
            else:
                message = 'Unable to create movie record.'

            return jsonify(
                data=results,
                message=message,
                statusCode=200,
                method='POST/ID'
            )

    @app.route('/movies/<movie_id>', methods=['GET'])
    def get_movie_by_id(movie_id):

        if request.method == 'GET':
            results = get_by_id(movie_id)
            message = ''
            if len(results):
                message = f'Found {len(results)} results.'
            return jsonify(
                data=results,
                message=message,
                statusCode=200,
                method='GET/ID'
            )
