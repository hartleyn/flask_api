import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
	return '<h1>Welcome Home</h1>'


matches = [
	{'id': 0,
	 'round': 1,
	 'points': 0,},
	{'id': 1,
	 'round': 2,
	 'points': 0,},
]


@app.route('/api', methods=['GET'])
def api_endpoint():
	return jsonify(matches)


@app.route('/api/matches', methods=['GET'])
def matches_endpoint():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for match in matches:
        if match['id'] == id:
          results.append(match)

    return jsonify(results)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
	
			
if __name__ == '__main__':
	app.run()
