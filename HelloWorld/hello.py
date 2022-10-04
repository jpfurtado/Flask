# Importação da microframework Flask  
from flask import Flask
app = Flask(__name__)
# Rota é o caminho relativo do seu site a URL que será acessada
@app.route("/")
# Função é o que será executado 
def hello():
    return "<H1>Hello World!!!</H1>"
@app.route("/usuarios/<usuario>")
def usuarios(usuario):
    return ("<H2>Hello, " + usuario + "</H2>" )
# Coloca o site no ar
if __name__ == '__main__':
    app.run(debug=True)
    
