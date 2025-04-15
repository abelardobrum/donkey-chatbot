import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

nltk.download('punkt')

class Chatbot:
    def __init__(self):
        self.historico = []
        self.ultimo_suplemento = None
        self.ultima_pergunta = None
        
        pares = [
            [
                r"oi|olá|Ola|e ai|fala ai|e aí|fala aí|fala|blz|beleza|como vai|tudo bem|tudo bom|bom dia|boa tarde|boa noite|salve|opa|coé|coe|eae|eai|yo|hey|oii|oiie|oie",
                ["Olá!", "Como posso ajudar você?", "Oi, como está?", "Olá! Tudo bem? "],
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
            ],
            [
                r"(.*)quem e você|quem é você|quem é|o que você faz|sobre o que você sabe|qual seu nome",
                ["Eu sou o Shallow Seek, um chatbot programado para te falar sobre suplementos! Sobre qual suplemento você quer saber?"]
            ]
            
        ]

        self.chat = Chat(pares, reflections)

    def respond(self, user_input):
            resposta = self.chat.respond(user_input)
            self.historico.append({"usuario": user_input, "resposta": resposta})
            return resposta

    def processar_mensagem(self, mensagem):
        mensagem_original = mensagem
        mensagem = mensagem.lower()
        tokens = set(word_tokenize(mensagem))

        suplementos = ["creatina", "whey", "glutamina"]

        for suplemento in suplementos:
            if suplemento in tokens:
                self.ultimo_suplemento = suplemento

        if "como" in tokens and "tomar" in tokens:
            self.ultima_pergunta = "como_tomar"
        elif "benefício" in tokens or "beneficios" in tokens or "benefícios" in tokens:
            self.ultima_pergunta = "beneficios"
        elif "serve" in tokens or "pra que" in mensagem or "para que" in mensagem:
            self.ultima_pergunta = "para_que_serve"

        if self.ultimo_suplemento:
            if self.ultima_pergunta == "como_tomar":
                if self.ultimo_suplemento == "creatina":
                    return "A creatina deve ser tomada diariamente, com ou sem treino. A dose recomendada é de 3 a 5g por dia, preferencialmente após o treino."
                elif self.ultimo_suplemento == "whey":
                    return "O whey protein deve ser tomado após o treino. Uma dose comum é de 20 a 30g com água ou leite."
                elif self.ultimo_suplemento == "glutamina":
                    return "A glutamina pode ser tomada em jejum, após o treino ou antes de dormir. A dose média é de 5g por dia."
            elif self.ultima_pergunta == "beneficios":
                if self.ultimo_suplemento == "creatina":
                    return "Os principais benefícios da creatina são: aumento de força e potência, melhora no desempenho em exercícios intensos e crescimento muscular."
                elif self.ultimo_suplemento == "whey":
                    return "Os benefícios do whey incluem: ganho de massa muscular, recuperação muscular acelerada, praticidade na ingestão de proteína e auxílio no emagrecimento."
                elif self.ultimo_suplemento == "glutamina":
                    return "A glutamina oferece benefícios como: fortalecimento do sistema imunológico, recuperação muscular e melhora da saúde intestinal."
            elif self.ultima_pergunta == "para_que_serve":
                if self.ultimo_suplemento == "creatina":
                    return "A creatina serve para aumentar a força, potência e volume muscular, além de melhorar a performance em exercícios de alta intensidade."
                elif self.ultimo_suplemento == "whey":
                    return "O whey protein é uma proteína de rápida absorção que auxilia no ganho de massa muscular e na recuperação pós-treino."
                elif self.ultimo_suplemento == "glutamina":
                    return "A glutamina auxilia na recuperação muscular, na imunidade e na saúde intestinal."

        if mensagem in suplementos:
            self.ultimo_suplemento = mensagem
            return f"Você gostaria de saber os benefícios ou como tomar {mensagem}?"


        if self.ultimo_suplemento is None:
            if self.ultima_pergunta == "como_tomar":
                return "Você quer saber como tomar qual suplemento? Creatina, whey ou glutamina?"
            elif self.ultima_pergunta == "beneficios":
                return "Você quer saber os benefícios de qual suplemento? Creatina, whey ou glutamina?"
            elif self.ultima_pergunta == "para_que_serve":
                return "Você quer saber para que serve qual suplemento? Creatina, whey ou glutamina?"

        return self.chat.respond(mensagem_original)