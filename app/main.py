import random
import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

# Baixar recursos do NLTK
nltk.download('punkt')

# Classe do chatbot com padrões de resposta
class Chatbot:
    def __init__(self):
        pares = [
            [
                r"oi|olá|Ola|e ai|fala ai|e aí|fala aí|fala|blz|beleza|como vai|tudo bem|tudo bom|bom dia|boa tarde|boa noite|salve|opa|coé|coe|eae|eai|yo|hey|oii|oiie|oie",
                ["Olá!", "Como posso ajudar você?", "Oi, como está?", "Olá! Está buscando informações sobre algum suplemento especifico? ", "Olá! O que posso te ajudar com informações de suplementos?"],
            ],
            [
                r"(.*)suplemento(.*)",
                ["Com qual suplemento você quer ajuda? Posso te falar sobre creatina, whey e glutamina."]
            ],
            [
                r"(.*)creatina(.*)como tomar(.*)|(.*)como tomar(.*)creatina(.*)",
                ["A creatina deve ser tomada diariamente, com ou sem treino. A dose recomendada é de 3 a 5g por dia, preferencialmente com uma refeição ou junto com o pós-treino."]
            ],
            [
                r"(.*)whey(.*)como tomar(.*)|(.*)como tomar(.*)whey(.*)",
                ["O whey protein deve ser tomado após o treino para otimizar a recuperação muscular. A dose comum é de 20 a 30g com água ou leite."]
            ],
            [
                r"(.*)glutamina(.*)como tomar(.*)|(.*)como tomar(.*)glutamina(.*)",
                ["A glutamina pode ser tomada em jejum, no pós-treino ou antes de dormir. A dose média é de 5g por dia."]
            ],
            [
                r"(.*)creatina(.*)",
                ["Você quer saber como tomar creatina ou para que ela serve?"]
            ],
            [
                r"(.*)whey(.*)",
                ["Você quer saber como tomar whey ou seus benefícios?"]
            ],
            [
                r"(.*)glutamina(.*)",
                ["Você quer saber como tomar glutamina ou para que ela serve?"]
            ],
            [
                r"(.*)obrigado(.*)|valeu|agradecido",
                ["De nada! Se precisar de mais informações sobre suplementos, é só chamar."]
            ],
            [
                r"(.*)tchau|sair|adeus",
                ["Até a próxima! Bons treinos e boa suplementação."]
            ]
        ]

        self.chat = Chat(pares, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)


    def processar_mensagem(self, mensagem):
        mensagem = mensagem.lower()
        tokens = set(word_tokenize(mensagem))

        # COMO TOMAR
        if "como" in tokens and "tomar" in tokens:
            if "creatina" in tokens:
                return "A creatina deve ser tomada diariamente, com ou sem treino. A dose recomendada é de 3 a 5g por dia, preferencialmente após o treino."
            elif "whey" in tokens:
                return "O whey protein deve ser tomado após o treino. Uma dose comum é de 20 a 30g com água ou leite."
            elif "glutamina" in tokens:
                return "A glutamina pode ser tomada em jejum, após o treino ou antes de dormir. A dose média é de 5g por dia."
            else:
                return "Você quer saber como tomar creatina, whey ou glutamina? Me diga qual."

        # QUANDO TOMAR
        if "quando" in tokens and "tomar" in tokens:
            if "creatina" in tokens:
                return "O melhor momento para tomar creatina é após o treino, mas o mais importante é tomar todos os dias, mesmo nos dias de descanso."
            elif "glutamina" in tokens:
                return "Você pode tomar glutamina em jejum, antes de dormir ou no pós-treino."
            elif "whey" in tokens:
                return "O whey é ideal para ser tomado logo após o treino."

        # PARA QUE SERVE / SERVE PRA QUE / PRA QUE SERVE
        if "serve" in tokens:
            if "creatina" in tokens:
                return "A creatina serve para aumentar a força, potência e volume muscular, além de melhorar a performance em exercícios de alta intensidade."
            elif "whey" in tokens:
                return "O whey protein é uma proteína de rápida absorção que auxilia no ganho de massa muscular e na recuperação pós-treino."
            elif "glutamina" in tokens:
                return "A glutamina auxilia na recuperação muscular, na imunidade e na saúde intestinal."
            else:
                return "Você quer saber para que serve creatina, whey ou glutamina? Me diga qual."

        # BENEFÍCIOS
        if "benefício" in tokens or "beneficios" in tokens or "benefícios" in tokens:
            if "creatina" in tokens:
                return "Os principais benefícios da creatina são: aumento de força e potência, melhora no desempenho em exercícios intensos e crescimento muscular."
            elif "whey" in tokens:
                return "Os benefícios do whey incluem: ganho de massa muscular, recuperação muscular acelerada, praticidade na ingestão de proteína e auxílio no emagrecimento."
            elif "glutamina" in tokens:
                return "A glutamina oferece benefícios como: fortalecimento do sistema imunológico, recuperação muscular e melhora da saúde intestinal."
            else:
                return "Você quer saber os benefícios de qual suplemento? Creatina, whey ou glutamina?"

        return self.chat.respond(mensagem)
