from flask import Flask, render_template, request, jsonify
from RSA import rsa

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('mainpage.html')


@app.route("/process", methods=['POST','GET'])
def process():
    input1 = request.form['userInput1']
    input2 = request.form['userInput2']
    input3 = request.form['userInput3']
    input4 = request.form['userInput4']
    if input1 and input2 and input3 and input4:
        result = rsa(int(input1), int(input2), int(input3), int(input4))
        return jsonify(result)
    return jsonify({'error': "Missing data!"})


# @app.route("/_crypt", methods=['POST'])
# def crypt():
#     en_de_crypt = request.form['en_de']


if __name__ == "__main__":
    # Running standalone
    app.run(debug=True, host="0.0.0.0")

