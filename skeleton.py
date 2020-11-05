from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('mainpage.html')


@app.route("/_choose", methods=['POST'])
def choose():
    cryptsys = request.form['cryptosystem']
    if cryptsys == "RSA":
        return render_template("rsa.html")
    elif cryptsys == "Diffie–Hellman key exchange":
        return render_template("Diffie–Hellman.html")
    elif cryptsys == "ElGamal encryption":
        return render_template("ElGamal.html")


# @app.route("/_crypt", methods=['POST'])
# def crypt():
#     en_de_crypt = request.form['en_de']


if __name__ == "__main__":
    # Running standalone
    app.run(debug=True, host="0.0.0.0")

