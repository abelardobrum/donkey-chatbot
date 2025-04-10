from flask import Blueprint, render_template, request, jsonify
from app.main import Chatbot

# Blueprint
bp = Blueprint('suplementos', __name__)

# Inicializa o chatbot
try:
    chatbot = Chatbot()
except Exception as e:
    print(f"Erro ao inicializar o chatbot: {str(e)}")
    chatbot = None

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/chat', methods=['POST'])
def chat():
    try:
        if not chatbot:
            return jsonify({
                'resposta': 'Desculpe, o chatbot está temporariamente indisponível. Por favor, tente novamente mais tarde.'
            }), 500

        data = request.get_json()
        
        if not data or 'mensagem' not in data:
            return jsonify({
                'resposta': 'Por favor, envie uma mensagem válida.'
            }), 400
            
        mensagem = data['mensagem']
        
        if not isinstance(mensagem, str) or not mensagem.strip():
            return jsonify({
                'resposta': 'Por favor, envie uma mensagem válida.'
            }), 400
            
        resposta = chatbot.processar_mensagem(mensagem)
        
        if not resposta:
            return jsonify({
                'resposta': 'Desculpe, não consegui processar sua mensagem. Por favor, tente novamente.'
            }), 500
            
        return jsonify({
            'resposta': resposta
        })
        
    except Exception as e:
        print(f"Erro no endpoint /chat: {str(e)}")
        return jsonify({
            'resposta': 'Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente.'
        }), 500
