from flask import Flask

app = Flask(__name__) 


@app.route("/")
@app.route('/bom-dia')
def boas_vindas():
  return "Seja Bem-vindo"

@app.route('/boa-tarde')
def boa_tarde():
  return "Boa tarde"

@app.route("/um/caminho/com/varios/elementos")
def um_caminho_longo():
    return "Hello World!"	


# main é o metodo principal
if __name__ == "__main__":
  app.run(host = 'localhost', port = 5002, debug = True )

