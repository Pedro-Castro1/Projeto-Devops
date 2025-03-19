from flask import Flask, jsonify, request
from users import users

app = Flask (__name__)


@app.route('/alunos/', methods=['GET'])
@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = users['Alunos']
    return jsonify(alunos)

@app.route('/alunos/<id>', methods=['GET'])
def alunoPorId(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({'mensagem': 'ID inserido para aluno tem que ser um numero inteiro'}), 400
    
    if id <=0:
        return jsonify({'mensagem': 'ID do aluno nao pode ser menor ou igual a que zero'}), 400
    
    alunos = users['Alunos']
    for aluno in alunos:
        if aluno['id'] == id:
            return jsonify(aluno)
    
    
    return jsonify({'mensagem': 'Aluno(a) nao encontrado(a)/inexistente'}), 404


@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dict = request.json
    

    chaves_esperadas = {'nome', 'idade', 'turma_id', 'data_nascimento','nota_primeiro_semestre', 'nota_segundo_semestre', 'media_final'}
    chaves_inseridas = set(dict.keys())
    chaves_invalidas = chaves_inseridas - chaves_esperadas
    if chaves_invalidas:
        return jsonify({
         'mensagem': 'Chaves adicionais não necessárias, retire-as',
            'chaves_invalidas': list(chaves_invalidas)
        }),400  
    if not dict.get('nome') or not dict.get('turma_id'):
        return jsonify({'mensagem': 'Para criar um novo professor preciso que voce me passe os parâmetros nome e turma'}), 400
    
    if 'idade' not in dict:
        return jsonify({'mensagem': 'Idade e obrigatoria, por favor insira-a'}), 400
    
    if not isinstance(dict['nome'], str) or not isinstance(dict['turma'], str):
        return jsonify({'mensagem': 'Os parametros nome e/ou  precisam ser do tipo STRING'}), 400
    
    if not isinstance(dict['idade'], int):
        return jsonify({'mensagem': 'Idade precisa ser um número INTEIRO'}), 400
    
    if not isinstance(dict['nota_primeiro_semestre'], (int, float)) or not isinstance(dict['nota_segundo_semestre'](int, float))or not isinstance(dict['media_final'](int, float)):
        return jsonify({'mensagem':'O parametro das notas dos semestres e/ou media final precisa ser um número do tipo float ou int'}), 400
    
    if dict['idade'] >= 0 and dict['idade'] < 6:
        return jsonify({'mensagem': 'Um aluno precisa ter no minimo 6 anos'}), 400

    if dict['idade'] >= 0 and dict['idade'] >= 20:
        return jsonify({'mensagem': 'esse aluno não pode estar matriculado nessa instituição de ensino, idade muito alta'}), 400

    if dict['idade'] < 0:
        return jsonify({'mensagem': 'Idade não pode ser negativa!!'}), 400

    if not isinstance (dict['turma_id'](int)):
        return jsonify({'mensagem': 'o ID de turma PRECISA ser um numero INTEIRO'}), 400
    
    else:
        ('NOT FOUND 404')
    
    
    id_novo = max([Alunos['id'] for Alunos in users['Alunos']]) + 1
    dict['id'] = id_novo
    users['Alunos'].append(dict)

    return jsonify(users['Alunos']), 201 
    
    