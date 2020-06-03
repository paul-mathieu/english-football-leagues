from flask import Flask, request, jsonify, render_template

import footballAPI

app = Flask(__name__)

# @app.route('/response', methods=['GET'])
# def response():
#     #choix_api = request.form.get("choixAPI")
#     #typeP = request.form.get("choixAPI")
#     parameters_dictionary = {}
#     for arg in request.args:
#         parameters_dictionary[arg] = request.args[arg]
#
#     #return render_template("index.html", choix_api=choix_api, typeP=typeP)
#     return render_template("index.html", parameters=parameters_dictionary)


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
        #return render_template("index.html", parameters=parameters_dictionary)
        #return render_template("recherche.php")


if __name__ == '__main__':
    app.run(debug=True)  # debug mode
