from flask import Flask, request, jsonify

import footballAPI

app = Flask(__name__)


@app.route("/")
def user_request():
    parameters_dictionary = {}
    for arg in request.args:
        parameters_dictionary[arg] = request.args[arg]

    client = footballAPI.FootballAPI()
    result = client.set_parameters(parameters_dictionary)
    if result is not None:
        return result
    else:
        return {"Error ": "No data"}


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
