from flask import Flask, request, session
from flask import  redirect, render_template
import os

app = Flask(__name__)

# Exercício: Use uma chave verdadeiramente segura lida do env ou de
# algum outro lugar seguro para que ela não apareça diretamente no
# código-fonte.
app.secret_key = os.getenv("SECRET_KEY")

usuarios = [
    {"login": "Maria", "senha": "1234"},
    {"login": "Roberto", "senha": "4321"},
    {"login": "Carlos", "senha": "abcd"},
    {"login": "Paula", "senha": "xyz"},
    {"login": "Chad", "senha": "based"},
]

def valida_login(login, senha):
    if len(login) == 0 or len(senha) == 0:
        return None 
    return type(login) == str and type(senha) == str


def verificar_login(login, senha):
    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            return u
    return None


@app.route("/login")
def form_login():
    session_contents = dict(session)
    print('session aqui:', session_contents)

    if "logado" in session:
        return redirect("/dashboard")
    return render_template("login.html", err="")

@app.route("/")
@app.route("/dashboard")
def dashboard():
    if "logado" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["logado"])

@app.route("/login", methods = ["POST"])
def fazer_login():
    # Exercício: Validar se os campos do form da requisição estão
    # corretos.
    login = request.form.get("login", "")
    senha = request.form.get("senha", "")

    if not valida_login(login, senha):
       return render_template("login.html", err="Campo vazio"), 302

    logado = verificar_login(login, senha)
    if logado is None:
        return render_template("login.html", err="Senha errada"), 302
    
    session["logado"] = logado
    return redirect("/dashboard")

@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("logado", None)
    return render_template("login.html", err="Tchau.")

if __name__ == "__main__":
    app.run(host = "localhost", port = 5000, debug = True)