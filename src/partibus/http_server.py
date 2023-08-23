"""
Simple HTTP server to provide REST APIs.
"""

import flask
import flask_cors

import partibus

app = flask.Flask(__name__)
cors = flask_cors.CORS(app)


@app.route("/")
def root():
    """
    Home page.
    """
    return flask.redirect("https://github.com/lutetiensis/partibus/", code=302)


@app.route("/lemmatize", methods=['POST'])
def lemmatize():
    """
    Lemmatize API
    """
    data = flask.request.json
    return flask.jsonify(partibus.lemmatize(data["words"]))


if __name__ == '__main__':
    app.run()
