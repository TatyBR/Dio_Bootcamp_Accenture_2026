# Avaliação e Métricas

## Formas de como avaliar o Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Definindo perguntas e respostas esperadas;
2. **Feedback real:** Pedir para outras pessoas testarem o agente e darem notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ ] Correto  [X] Incorreto
- **Observações:** Por limitações do modelo utilizado (llama3.2:3b), não houve resposta correto. O modelo não consegue realizar os cálculos.

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [ ] Correto  [X] Incorreto
- **Observações:** Mesmo realizado modificações no código, o modelo indica investimento quando perguntado.

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto Previdência Privada (PGBL/VGBL)?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [ ] Correto  [X] Incorreto
- **Observações:** Mesmo realizado modificações no código, o modelo informa o rendimento.

### Teste 5: Recomendação sobre vida financeira
- **Pergunta:** "Me traga 5 dicas de como melhorar minha vida financeira?"
- **Resposta esperada:** Agente deve atuar como um orientador financeiro pessoal
- **Resultado:** [X] Correto  [] Incorreto

### Teste 6: Explicação sobre algum investimento
- **Pergunta:** "Me traga 5 dicas de como melhorar minha vida financeira?"
- **Resposta esperada:** Agente deve atuar como um orientador financeiro e responder corretamente sobre a dúvida
- **Resultado:** [X] Correto  [] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Orientações sobre a vida financeira.
- Não informar sobre o que é fora do escopo.

**O que pode melhorar:**
- O modelo indicado na aula para uso foi o **gpt-oss**, mas devido limitações de hardware isso não foi possível.
- Para continuar no desenvolvimento, foi instalado o modelo **llama3.2:3b**, mas este modelo trás muitas limitações. Foram realizados alguns ajustes no próprio código Python, inclusive o uso da biblioteca **Guardrails** para que o modelo respondesse bem ao que foi determinado, mas não houve muito sucesso, pois o modelo não respeitou as regras impostas no system prompt. 
- Para melhorar: Usar uma API de LLM na nuvem (sair do uso da LLM local).

---

## Métricas Avançadas que podem ser utilizadas posteriormente:

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!