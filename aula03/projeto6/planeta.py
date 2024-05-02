from flask import Flask, render_template, flash
app = Flask(__name__)

app.secret_key = "sua_chave_secreta_aqui"

@app.route("/visitar/<planeta>")
def visitar_planeta(planeta):
    flash(f"Você visitou o planeta {planeta} recentemente!", "info")
    return "OK"

@app.route("/")
@app.route("/planetas")
def listar_planetas_visitados_recentemente():
    return render_template("planetas.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)