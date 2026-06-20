import pandas as pd
import json
import requests
import streamlit as st
from guardrails_custom import validar_resposta

# ======== Configurações Olllama ========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO ="llama3.2:3b"

# ======== carregando a base de conheciemento ========
with open('./data/perfil_investidor.json', 'r', encoding='utf-8') as f:
   perfil = json.load(f)
with open('./data/transacoes.csv', 'r', encoding='utf-8') as f:
   transacoes = pd.read_csv(f)
with open('./data/historico_atendimento.csv', 'r', encoding='utf-8') as f:
   historico = pd.read_csv(f)
with open('./data/produtos_financeiros.json', 'r', encoding='utf-8') as f:
   produtos = json.load(f)

# ======== contexto ==========

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, { perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DE INVESTIMENTO DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ======== System Prompt ========
system_prompt = f"""
Você é Sofi, uma educadora financeira amigável e didática.
Seu objetivo é ensinar conceitos de finanças pessoais de forma simples, usando exemplos práticos com os dados financeiros do cliente.

REGRAS OBRIGATÓRIAS:
1. NUNCA recomende investimentos específicos (ações, fundos, corretoras, etc). Apenas EXPLIQUE como tipos de investimento funcionam, de forma geral.
2. Se a pergunta NÃO for sobre finanças pessoais, NÃO responda o conteúdo da pergunta. Em vez disso, responda exatamente nesse estilo:
   "Eu sou especialista em finanças pessoais, então não consigo te ajudar com isso! Mas posso te explicar sobre [sugestão de tema financeiro relacionado, se fizer sentido]."
3. Use os dados do cliente fornecidos no CONTEXTO para dar exemplos personalizados.
4. Linguagem simples, como se estivesse explicando pra um amigo sem nenhum conhecimento técnico.
5. Se não souber algo, diga: "Não tenho essa informação, mas posso explicar..."
6. NUNCA critique a vida financeira do cliente. Apenas oriente, e só aconselhe se for pedido.
7. Responda em no máximo 2 parágrafos, de forma clara e direta.
8. Sempre termine perguntando se o cliente entendeu.

Lembre-se: você SÓ fala sobre finanças pessoais. Qualquer outro assunto, recuse educadamente conforme a regra 2.
"""

# ======== Chamar Ollama ========
def perguntar(msg):
   prompt = f"""
   {system_prompt}

   CONTEXTO DO CLIENTE:
   {contexto}

   Pergunta: {msg}"""
   
   r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
   print(r.status_code, r.text)
   return r.json()['response']

 # ======== Camada Guardrails: valida antes de retornar ========
   resultado = validar_resposta(resposta_bruta)
   if not resultado["valido"]:
       print(f"[GUARDRAILS] Resposta bloqueada: {resultado['motivo']}")  # debug no terminal

   return resultado["resposta_final"]

# ======== Interface Streamlit ========
st.title("💵 Sofi - Educadora Financeira 💵")

# ======== Inicializa o histórico (só na primeira vez) ========
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

# ======== Redesenha todo o histórico já existente ========
for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

# ======== Processa nova pergunta ========
if pergunta := st.chat_input("Qual a sua dúvida sobre finanças pessoais? "):
    st.chat_message("user").write(pergunta)
    st.session_state.mensagens.append({"role": "user", "content": pergunta})

    with st.spinner("Sofi está pensando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})



