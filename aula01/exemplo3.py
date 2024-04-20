from flask import Flask

app = Flask(__name__)

casais_e_filhos = {
    "camila,paulo": ["Pedro", "Carlos", "Mariana"],
    "laura,joaquim": ["Sandra", "Daniela"],
    "rafaela,fernando": ["Larissa", "Marcos", "Vanessa", "Andressa"],
    "maria,andre": ["Juliano"],
    "tatiana,luis": ["Kelly", "Kelvin", "Karla"],
    "beatriz,jose": ["João", "Marcelo", "Guilherme"],
    "tamara,rodolfo": []
}

def filhos(mae, pai):
    casal = f"{mae.lower()},{pai.lower()}"

    if casal not in casais_e_filhos: return None

    filhos = casais_e_filhos[casal]
    if len(filhos) == 0: return "O casal não tem filhos."
    
    if len(filhos) == 1:
        return f"O casal tem 1 filho(a): {filhos[0]}."
    return f"O casal tem {len(filhos)} filhos(as): " \
        + f"{ ', '.join(filhos[:-1])} e {filhos[-1]}."

@app.route("/casal/<mae>/<pai>/filhos")
def encontrar_filhos(mae, pai):
    f = filhos(mae, pai)
    if f is None: return "Casal não encontrado."
    return f

if __name__ == "__main__":
    app.run(host = 'localhost', port = 5002, debug = True)