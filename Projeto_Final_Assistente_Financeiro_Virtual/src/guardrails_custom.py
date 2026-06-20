# guardrails_custom.py
"""
Validador customizado simples para o agente Sofi.
Desenvolvido apelas com lógica Python.
"""

import re

# Padrões de linguagem que indicam recomendação PESSOAL/DIRECIONADA
# (em vez de explicação neutra de como algo funciona)
PADROES_RECOMENDACAO = [
    r"eu recomendar[ia|ei]",
    r"recomendo (o|a|que)",
    r"seria ideal (pra|para) você",
    r"um bom (ponto de partida|produto|investimento) seria",
    r"voc[eê] deveria (investir|comprar|aplicar)",
    r"sugiro (que voc[eê]|investir|comprar)",
    r"a melhor (op[cç][aã]o|escolha) (seria|[eé])",
    r"come[cç]ar com (um|uma|o|a) (fundo|a[cç][aã]o|cdb|tesouro|cripto)",
    r"invista (em|no|na)",
    r"compre (a[cç][oõ]es|cripto|bitcoin|fundos)",
]

# Palavras/temas que indicam recomendação de investimento específico
PALAVRAS_INVESTIMENTO_PROIBIDO = [
    "compre ações", "invista em", "recomendo a corretora",
    "tesouro direto da", "fundo imobiliário específico",
    "compre bitcoin", "compre criptomoeda", "ação da",
    "cdb do banco", "invista no banco", "recomendo o fundo", "melhor investimento é",
    "eu recomendo o Fundo Multimercado (FMI)",  "eu recomendo o Fundo de Ações (FAI)",
    "eu recomendo o Tesouro Selic", "eu recomendo o CDB Liquidez Diária", "eu recomendo o LCI/LCA",
    "eu recomendo o Tesouro IPCA+", "eu recomendo o CDB CRI/CRA", "eu recomendo Debêntures Incentivadas",
    "eu recomendo o Fundo Multimercado", "eu recomendo o Fundo de Ações", "eu recomendo o FII (Fundo de Investimento Imobiliário)",
    "eu recomendo o ETF (Exchange Traded Fund)",  "eu recomendo o FBDR (Brazilian Depositary Receipt)",
    "eu recomendo o Previdência Privada (PGBL/VGBL)",  "eu recomendo começar com um"
]


# Palavras que indicam que a resposta fugiu do tema de finanças
TEMAS_FORA_DE_CONTEXTO = [
    "receita de", "ingredientes", "modo de preparo",
    "futebol", "filme", "série", "novela",
    "código python", "função javascript", "história da arte", "música", "viagem",
    "previsão do tempo", "notícias", "política", "saúde", "medicina", "fruta", "culinária"
]

FRASE_PADRAO_RECUSA = (
    "Eu sou especialista em finanças pessoais, então não consigo "
    "te ajudar com isso! Mas posso te explicar sobre outros temas "
    "financeiros, como orçamento, investimentos ou planejamento. "
    "Quer tentar de novo? 😊"
)

FRASE_RECUSA_INVESTIMENTO = (
    "Não posso recomendar produtos de investimento específicos — isso "
    "exige análise de um profissional certificado e do seu perfil completo. "
    "Mas posso te explicar como esse tipo de investimento funciona, "
    "quais são os riscos e vantagens em geral, e te ajudar a entender "
    "o que considerar antes de decidir. Quer que eu explique?"
)

def validar_resposta(texto_resposta: str) -> dict:
    texto_lower = texto_resposta.lower()

    # Checagem 1: recomendação direcionada de investimento
    for padrao in PADROES_RECOMENDACAO + PALAVRAS_INVESTIMENTO_PROIBIDO:
        if re.search(padrao, texto_lower):
            return {
                "valido": False,
                "motivo": f"Padrão de recomendação detectado: '{padrao}'",
                "resposta_final": FRASE_RECUSA_INVESTIMENTO
            }

    # Checagem 2: fuga de tema
    for termo in TEMAS_FORA_DE_CONTEXTO:
        if termo in texto_lower:
            return {
                "valido": False,
                "motivo": f"Possível fuga de tema detectada: '{termo}'",
                "resposta_final": FRASE_PADRAO_RECUSA
            }

    return {
        "valido": True,
        "motivo": None,
        "resposta_final": texto_resposta
    }