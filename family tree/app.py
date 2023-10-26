# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    nome = "Flávia" # escreva seu nome
    idade = "13" # escreva sua idade

    return render_template('index.html' , nome = nome , idade = idade)

# defina a rota para a página do pai
@app.route("/pai")
def home():
    name="Altair"
    idade="46"

# defina a rota para a página da mãe
@app.route("/mãe")
def home():
    name="Márcia"
    idade="45"

# defina a rota para a página do amigo
@app.route("/anita")
def home():
    name="Anita"
    idade="13"

# adicione outras rotas, se você quiser
@app.route("/manuela")
def home():
    name="Manuela"
    idade="8"



# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
