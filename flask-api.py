from flask import Flask, request, jsonify

import footballAPI

app = Flask(__name__)

@app.route("/")
def hello():
    parameters_dictionary={}
    for arg in request.args:
        parameters_dictionary[arg] = request.args[arg]

    client = footballAPI.FootballAPI()
    return (client.set_parameters(parameters_dictionary))

if __name__ == '__main__':
    app.run(debug=True) #debug mode