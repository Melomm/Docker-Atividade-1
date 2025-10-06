from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados do currículo
    curriculo = {
        'nome': 'Marcelo',
        'cargo': 'Engenharia de Computação e Modelador 3D',
        'email': 'aaaaaaaaaaa@gmail.com',
        'telefone': 'numero',
        'linkedin': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'github': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'resumo': 'py ton :)',
        'habilidades': [
            'Python',
            'Flask/FastAPI',
            'Docker',
            'Git/GitHub',
            'HTML/CSS',
            'JavaScript',
            'SQL',
            'B L E N D E R'
        ],
        'experiencias': [
            {
                'cargo': 'Cargo super legal',
                'empresa': 'www.google.com',
                'periodo': '1985 - Atual',
                'descricao': 'Não sei onde estou'
            },
            {
                'cargo': 'Freelancer',
                'empresa': 'Autônomo',
                'periodo': 'datas legais',
                'descricao': '3d'
            }
        ],
        'formacao': [
            {
                'curso': 'Eng comp',
                'instituicao': 'Opa',
                'periodo': '2024 - 2027',
                'status': 'Cursando'
            }
        ],
        'projetos': [
            {
                'nome': 'Currículo Containerizado',
                'descricao': 'Aplicação web em Flask para exibição de currículo, containerizada com Docker.',
                'tecnologias': 'Python, Flask, Docker, HTML/CSS'
            },
            {
                'nome': 'API REST com FastAPI',
                'descricao': 'API REST para gerenciamento de tarefas com autenticação JWT.',
                'tecnologias': 'Python, FastAPI, PostgreSQL, Docker'
            }
        ]
    }
    
    return render_template('index.html', curriculo=curriculo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)