from flask import Flask

app = Flask(__name__)

cores_frutas = {
    "morango": "vermelho",
	  "uva": "roxo",
    "banana": "amarelo",
    "abacaxi": "amarelo",
    "limão": "verde"
}

@app.route('/')
def rota_padrao():
  return 'Hello World'

@app.route("/frutas/<nome_fruta>/cor")
def frutas(nome_fruta):
  if nome_fruta in cores_frutas:
    return cores_frutas[nome_fruta]
  return "Not found"

if __name__ == "__main__":
  app.run(host = 'localhost', port = 5002, debug = True)