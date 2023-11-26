import time

from flask import Flask, render_template, request

app = Flask(__name__)

valor3 = 0
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/valor1', methods=['POST'])
def valor1():
    valor1 = request.form['input_v1']
    print(f"Valor 1: {valor1}")
    return render_template('index.html', valorprimeiro = valor1)

@app.route('/valor2', methods=['POST'])
def valor2():
    valor2 = request.form['input_v2']
    print(f"O segundo valor é {valor2}")
    return render_template('index.html', valorsegundo = valor2)

def test():
    print("A soma do valor 1 e do valor 2 não pode ser feita porque os dois valores são string")
if __name__ == "__main__":
    app.run(debug=True)

