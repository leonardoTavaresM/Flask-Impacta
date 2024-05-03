from flask import Flask, jsonify, request

app = Flask(__name__)

database = {
    'ALUNO' : [{"id": 1, "nome": "Andreia"},
                {"id": 2, "nome": "Arthur"},
				{"id": 3, "nome": "Pedro"}],
				
    'PROFESSOR' : [{"id": 1, "nome": "Professor1"},
                {"id": 2, "nome": "Professor2"},
				{"id": 3, "nome": "Professor3"}],
}

@app.route('/alunos')
def getAlunos():
  return jsonify(database['ALUNO'])

@app.route('/professores')
def getProfessores():
  return jsonify(database['PROFESSOR'])

@app.route('/show_all')
def getAll():
  return jsonify(database)


@app.route('/alunos', methods=['POST'])
def inserir_aluno():
  novo_aluno = request.json
  database['ALUNO'].append(novo_aluno)
  return jsonify(database['ALUNO'])


if __name__ == '__main__':
  app.run(host = 'localhost', port = 5000, debug = True)