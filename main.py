# from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index ():
    return render_template("index.html")

@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])
    alt = altura ** 2
    imc = peso / alt
    if (imc < 18.5):
        tabela = 'Magreza'
    elif (imc >= 18.5) and (imc < 25):
        tabela = 'Normal'
    elif (imc >= 25) and (imc < 30):
        tabela = 'Sobrepeso'
    elif (imc >= 30) and (imc < 35):
        tabela = 'Obesidade Grau I'
    elif (imc >= 35) and (imc < 40):
        tabela = 'Obesidade Grau II'
    else:
        tabela = 'Obesidade Grau III'

    return render_template('index.html', resultado=f'Seu IMC é: {imc} - {tabela}')

if __name__ == '__main__':
    app.run(debug=True)