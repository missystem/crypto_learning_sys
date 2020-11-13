from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('mainpage.html')


@app.route("/_choose", methods=['POST'])
def choose():
    userInput1 = request.form['userInput1']
    userInput2 = request.form['userInput2']
    userInput3 = request.form['userInput3']
    print(userInput1)
    print(userInput2)
    print(userInput3)


# @app.route("/_crypt", methods=['POST'])
# def crypt():
#     en_de_crypt = request.form['en_de']


if __name__ == "__main__":
    # Running standalone
    app.run(debug=True, host="0.0.0.0")

