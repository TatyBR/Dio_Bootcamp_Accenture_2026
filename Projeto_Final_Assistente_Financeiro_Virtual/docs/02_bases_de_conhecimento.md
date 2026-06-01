# Base de Conhecimento

## Dados Utilizados

Os arquivos utilizados encontram-se na pasta `data` e são os seguintes:

| Arquivo | Formato | Para orientar a Sofi |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores auxiliando na continuidade do atendimento de maneira eficiente |
| `perfil_investidor.json` | JSON | Personalizar as explicações sobre as dúvidas e necessidades de aprendizagem do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser explicados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de maneira didática |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O arquivo `produtos_financeiros.json` foi atualizado para o ano de 2026, recebeu novos tipos de produtos (investimentos) e também um novo campo (elegibilidade) que descreve melhor para quem o produto é indicado e suas restrições.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Injetados diretamente no prompt ou carregados via código python.

```python

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```Text
DADOS E PERFIL DO CLIENTE:



TRANSAÇÕES DO CLIENTE:

PRODUTOS DISPONÍVEIS PARA ENSINO:

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
