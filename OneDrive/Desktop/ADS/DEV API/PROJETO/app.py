from flask import Flask, request, jsonify

#inicialização 15 pqp
app = Flask(__name__)

#dici dados
professores = [{"nome": "Caio", "Id": 1}]

turmas = [{"nome": "Desenvolvimento de API", "Id": 10}]

alunos = [{"nome": "Gabriel Lopes", "Id": 7}]

# Funções CRUD - Professores

@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify(professores)

@app.route('/professores/<int:id>', methods=['GET'])
def obter_professor(id):
    professor = next((p for p in professores if p['Id'] == id), None)
    return jsonify(professor) if professor else ("Professor não encontrado", 404)

@app.route('/professores', methods=['POST'])
def adicionar_professor():
    dados = request.json
    dados['Id'] = len(professores) + 1
    professores.append(dados)
    return jsonify({"mensagem": "Professor adicionado com sucesso!"}), 201

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    professor = next((p for p in professores if p['Id'] == id), None)
    if professor:
        professor.update(request.json)
        return jsonify({"mensagem": "Professor atualizado com sucesso!"})
    return ("Professor não encontrado", 404)

@app.route('/professores/<int:id>', methods=['DELETE'])
def deletar_professor(id):
    professor = next((p for p in professores if p['Id'] == id), None)
    if professor:
        professores.remove(professor)
        return jsonify({"mensagem": "Professor removido com sucesso!"})
    return ("Professor não encontrado", 404)

# Funções CRUD - Turmas

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify(turmas)

@app.route('/turmas/<int:id>', methods=['GET'])
def obter_turma(id):
    turma = next((t for t in turmas if t['Id'] == id), None)
    return jsonify(turma) if turma else ("Turma não encontrada", 404)

@app.route('/turmas', methods=['POST'])
def adicionar_turma():
    dados = request.json
    dados['Id'] = len(turmas) + 1
    turmas.append(dados)
    return jsonify({"mensagem": "Turma adicionada com sucesso!"}), 201

@app.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = next((t for t in turmas if t['Id'] == id), None)
    if turma:
        turma.update(request.json)
        return jsonify({"mensagem": "Turma atualizada com sucesso!"})
    return ("Turma não encontrada", 404)

@app.route('/turmas/<int:id>', methods=['DELETE'])
def deletar_turma(id):
    turma = next((t for t in turmas if t['Id'] == id), None)
    if turma:
        turmas.remove(turma)
        return jsonify({"mensagem": "Turma removida com sucesso!"})
    return ("Turma não encontrada", 404)

# Funções CRUD - Alunos

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify(alunos)

@app.route('/alunos/<int:id>', methods=['GET'])
def obter_aluno(id):
    aluno = next((a for a in alunos if a['Id'] == id), None)
    return jsonify(aluno) if aluno else ("Aluno não encontrado", 404)

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    dados = request.json
    dados['Id'] = len(alunos) + 1
    alunos.append(dados)
    return jsonify({"mensagem": "Aluno adicionado com sucesso!"}), 201

@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = next((a for a in alunos if a['Id'] == id), None)
    if aluno:
        aluno.update(request.json)
        return jsonify({"mensagem": "Aluno atualizado com sucesso!"})
    return ("Aluno não encontrado", 404)

@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    aluno = next((a for a in alunos if a['Id'] == id), None)
    if aluno:
        alunos.remove(aluno)
        return jsonify({"mensagem": "Aluno removido com sucesso!"})
    return ("Aluno não encontrado", 404)

# Execução do Flask
if __name__ == '__main__':
    app.run(debug=True)

