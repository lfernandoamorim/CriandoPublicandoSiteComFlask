#Tenha o Flask instalado antes de começar
#Para fazer o deploy com Flask, instalar > pip install gunicorn
# o "pip freeze > requirements.txt", é criado um pacote de tudo que tem no projeto

#importa o Flask
from flask import Flask, render_template

#para inicializar um aplicativo do Flask, precisa começar com isso
app = Flask(__name__)

#CRIA AS PÁGINAS EM FLASK

#route() é o que informa a página a ser criada, isto é, o caminho para abrir a página
#o @app (app porque chamaos de app lá em cima) é um decoretor, que é uma linha de 
# código que atribui em um endereço o que está na função (def)
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#cria uma página dinâmica, basta colocar um nome no endereço
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    #passa para o HTML o nome do usuário para a página usuario.html
    #EX.: http://127.0.0.1:5000/usuarios/Malibu, Imprime, Meu nome é Malibu
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#COLOCAR O SITE NO AR

#ao colocar o debug=True faz todas as edições rodarem automaticamente sem precisar parar o site
#o if fala que vai rodar o que tiver dentro dele se rodar o código diretamente
#mas se for importado por outro arquivo, não faz nada
#if __name__ == "__main__":
    #app.run(debug=True)
app.run(debug=True)

#Servidor Heroku é GRATUÍTO


