from flask import Flask,request, render_template, redirect, url_for
from luhn_algorithm import luhn_algorithm

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        return redirect(url_for('verify', card_number = request.form['card-number']))


@app.route('/verify/<card_number>', methods = ['GET'])
def verify(card_number):
    
    card_number = card_number.replace(" ", "")

    if card_number.isnumeric():
        
        message = luhn_algorithm(card_number)
        return render_template("credit_card.html", message = message)

    else:
        
        return render_template("credit_card.html", message = "El numero de la tarjeta contiene letras")

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='5000')


