import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template('mainpage.html')


@app.route("/_choose", methods=['POST'])
def choose():
    cryptsys = flask.request.form['cryptosystem']
    if flask.request.form['en/de'] == "Encrypt":
        if cryptsys == "RSA":
            return render_template("")
        elif cryptsys == "Diffie–Hellman key exchange":
            return render_template("")
        elif cryptsys == "ElGamal encryption":
            return render_template("")
    else:
        if cryptsys == "RSA":
            return render_template("")
        elif cryptsys == "Diffie–Hellman key exchange":
            return render_template("")
        elif cryptsys == "ElGamal encryption":
            return render_template("")

if __name__ == "__main__":
    # Running standalone
    app.run(debug=True, host="0.0.0.0")

