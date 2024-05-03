from flask import Flask, jsonify

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

if __name__ == '__main__':
  app.run(host = 'localhost', port = 5000, debug = True)