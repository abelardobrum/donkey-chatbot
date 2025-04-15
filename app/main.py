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
                ["A creatina deve ser tomada diariamente, com ou sem treino. A dose recomendada é de 3 a 5g por dia, preferencialmente com uma refeição ou junto com o pós-treino. Qual outro suplemento você quer saber como tomar?"]
            ],
            [
                r"(.*)creatina(.*)beneficios(.*)|(.*)beneficios(.*)creatina(.*)",
                ["A creatina melhora a força, potência e recuperação muscular, além de favorecer o ganho de massa magra, hidratação celular e desempenho em exercícios intensos. Também pode beneficiar a função cerebral, proteger contra doenças neurodegenerativas e auxiliar na saúde muscular em idosos. Quer saber mais o que sobre o este suplemento?"]
            ],
                        [
                r"(.*)creatina(.*)pra que serve?(.*)|(.*)para que serve(.*)creatina(.*)",
                ["A creatina serve para aumentar a produção de energia rápida nos músculos, melhorando o desempenho físico em atividades intensas e auxiliando no ganho de força, massa muscular e recuperação. Quer saber mais o que sobre o este suplemento?"]
            ],
            [
                r"(.*)whey(.*)como tomar(.*)|(.*)como tomar(.*)whey(.*)",
                ["O whey protein deve ser tomado após o treino para otimizar a recuperação muscular. A dose comum é de 20 a 30g com água ou leite. Qual outro suplemento você quer saber como tomar?"]
            ],
            [
                r"(.*)whey(.*)beneficios(.*)|(.*)beneficios(.*)whey(.*)",
                ["O whey protein ajuda na recuperação e no crescimento muscular, fornece proteína de alta qualidade com rápida absorção e contribui para o aumento de massa magra e manutenção da saúde geral. Quer saber mais o que sobre o este suplemento?"]
            ],
            [
                r"(.*)whey(.*)pra que serve(.*)|(.*)para que serve(.*)whey(.*)",
                ["O whey serve para suplementar a ingestão de proteínas, favorecendo a recuperação muscular, o ganho de massa magra e o suporte nutricional em dietas com maior demanda proteica. Quer saber mais o que sobre o este suplemento?"]
            ],
            [
                r"(.*)glutamina(.*)como tomar(.*)|(.*)como tomar(.*)glutamina(.*)",
                ["A glutamina pode ser tomada em jejum, no pós-treino ou antes de dormir. A dose média é de 5g por dia. Qual outro suplemento você quer saber como tomar?"]
            ],
            [
                r"(.*)glutamina(.*)beneficios(.*)|(.*)beneficios(.*)glutamina(.*)",
                ["A glutamina fortalece o sistema imunológico, auxilia na recuperação muscular, melhora a saúde intestinal e pode ajudar a reduzir o catabolismo em situações de estresse físico intenso. Quer saber mais o que sobre o este suplemento?"]
            ],
            [
                r"(.*)glutamina(.*)pra que serve(.*)|(.*)para que serve(.*)glutamina(.*)",
                ["A glutamina serve para apoiar a imunidade, preservar a massa muscular e melhorar a saúde intestinal, sendo útil especialmente em treinos intensos ou períodos de estresse. Quer saber mais o que sobre o este suplemento?"]
            ],
            [
                r"(.*)BCAA(.*)como tomar(.*)|(.*)como tomar(.*)BCAA(.*)",
                ["Não tome. Quer saber como tomar outro suplemento?"]
            ],
            [
                r"(.*)BCAA(.*)beneficios(.*)|(.*)beneficios(.*)BCAA(.*)",
                ["Não tem. Quer saber os beneficios de outro suplemento?"]
            ],
            [
                r"(.*)BCAA(.*)pra que serve(.*)|(.*)para que serve(.*)BCAA(.*)",
                ["Jogar dinheiro fora. Quer saber sobre outro suplemento?"]
            ],
            [
                r"(.*)creatina(.*)",
                ["Você quer saber como tomar creatina, para que ela serve, ou os benefícios?"]
            ],
            [
                r"(.*)whey(.*)",
                ["Você quer saber como tomar whey, pra que ele serve, ou seus benefícios?"]
            ],
            [
                r"(.*)glutamina(.*)",
                ["Você quer saber como tomar glutamina, para que ela serve ou seus benefícios?"]
            ],
            [
                r"(.*)BCAA(.*)",
                ["Você quer saber como tomar BCAA, para que ele serve ou seus benefícios?"]
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
                r"(.*)quem e voce|quem é você|quem é|o que você faz|sobre o que você sabe|qual seu nome",
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
        mensagem_lower = mensagem.lower()
        tokens = set(word_tokenize(mensagem_lower))

        suplementos = ["creatina", "whey", "glutamina", "bcaa"]

        for suplemento in suplementos:
            if suplemento in tokens:
                self.ultimo_suplemento = suplemento

        if {"como", "tomar"}.issubset(tokens) and self.ultimo_suplemento:
            mensagem_lower = f"como tomar {self.ultimo_suplemento}"

        elif "benefício" in tokens or "benefícios" in tokens or "beneficios" in tokens:
            if self.ultimo_suplemento:
                mensagem_lower = f"beneficios do {self.ultimo_suplemento}"
        elif (
            "serve" in tokens and (
                {"para", "que"}.issubset(tokens) or {"pra", "que"}.issubset(tokens)
            )
        ):
            if self.ultimo_suplemento:
                mensagem_lower = f"para que serve {self.ultimo_suplemento}"

        resposta = self.chat.respond(mensagem_lower)
        self.historico.append({"usuario": mensagem_original, "resposta": resposta})

        return resposta