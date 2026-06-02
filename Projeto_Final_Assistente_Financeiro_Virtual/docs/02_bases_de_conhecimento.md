# Base de Conhecimento

> [!TIP]
> Prompt utilizado para esta etapa:
> Preciso organizar a base de conhecimento do meu agente financeiro educativo.
> Tenho estes arquivos de dados: historico_atendimento.csv, perfil_investidor.json, produtos_financeiros.json e transacoes.csv.
> Me ajude a:
> 1. Entender o conteúdo de cada arquivo;
> 2. Decidir a melhor maneira de usar cada arquivo;
> 3. Criar um exemplo de contexto formatado para incluir no prompt.



## Dados Utilizados

Os arquivos utilizados encontram-se na pasta `data` e são os seguintes:

| Arquivo | Formato | Para orientar a Sofi |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Interações anteriores que serviram para contextualizar o agente e auxiliar na continuidade do atendimento de maneira eficiente |
| `perfil_investidor.json` | JSON | Usado para personalizar as explicações sobre as dúvidas e necessidades de aprendizagem do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser explicados ao cliente |
| `transacoes.csv` | CSV | Analisar o padrão de gastos do cliente e usar essas informações de maneira didática |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O arquivo `produtos_financeiros.json` foi atualizado para o ano de 2026. Recebeu novos tipos de produtos (investimentos) e também um novo campo (elegibilidade) que descreve melhor para quem o produto é indicado e suas restrições.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

1ª POSSIBILIDADE:
**** Injetados diretamente no prompt ou carregados via código python.

2ª POSSIBILIDADE:
Carregar via código python.
(Incluir abaixo o código utilizado!!!!!!)

```python

```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o agente tenha o melhor contexto possível. Lembrando que, em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```
    DADOS E PERFIL DO CLIENTE (perfil_investidor.json):

{
  "nome": "Gabriel Henrique",
  "idade": 32,
  "profissao": "Representante comercial",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 50000.00,
  "reserva_emergencia_atual": 100.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada compra novo veículo",
      "valor_necessario": 30000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE (transacoes.csv):

2026-02-20,Conta de Água,moradia,123.97,saida
2026-02-30,Convênio Médico,saude,310.01,saida
2026-02-20,Farmácia,saude,80.00,saida
2026-01-01,Salário,receita,12000.00,entrada
2026-01-10,Celular filho,lazer,60.20,saida
2026-01-25,Celular,lazer,180.00,saida
2026-01-10,Curso filho,educação,230.00,saida
2026-01-15,Fatura Cartão,alimentacao,5500.00,saida
2026-01-15,Internet,lazer,100.00,saida
2026-01-08,Conta de Luz,moradia,195.85,saida
2026-01-20,Conta de Água,moradia,123.97,saida
2026-01-30,Convênio Médico,saude,310.01,saida
2026-01-20,Farmácia,saude,80.00,saida

HISTÓRICO DE ATENDIMENTO DO CLIENTE (historico_atendimento.csv):

data,canal,tema,resumo,resolvido
2025-09-15,chat,CDB,Cliente perguntou sobre rentabilidade e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Tesouro Selic,Cliente pediu explicação sobre o funcionamento do Tesouro Direto,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso da reserva de emergência,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim


PRODUTOS DISPONÍVEIS PARA ENSINO:
...
 {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic (Selic Meta: 14,50% a.a. | maio/2026)",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes",
    "observacoes": "Liquidez diária com cobertura do Tesouro Nacional. Melhor opção para curto prazo.",
    "elegibilidade": {
      "publico_alvo": "Pessoa física brasileira",
      "idade_minima": "Qualquer idade (menores precisam de representante legal)",
      "perfil_investidor": "Conservador",
      "restricoes": "Nenhuma restrição relevante. Isenção de IR não se aplica a pessoa jurídica."
    }
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% a 105% do CDI (CDI: ~14,40% a.a. | maio/2026)",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário",
    "observacoes": "Cobertura do FGC até R$ 250 mil por CPF/instituição. Comparar taxas entre bancos.",
    "elegibilidade": {
      "publico_alvo": "Pessoa física ou jurídica brasileira",
      "idade_minima": "Qualquer idade (menores precisam de representante legal)",
      "perfil_investidor": "Conservador",
      "restricoes": "Pessoa jurídica está sujeita a tributação diferenciada (sem isenções). FGC cobre apenas PF e PJ de pequeno porte."
    }
...



## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto ilustrado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais relevantes, otimizado assim o consumo de tokens. Entretando, vale lembrar que mais importante do que economizar tokens é ter todas as informações relevantes disponíveis em seu contexto.

```
Dados do Cliente:
- Nome: Gabriel Herique
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 05/20: Supermercado - R$ 1500
- 05/15: Internet - R$ 100
- 05/22: Gasolina - R$ 300
- 05/28: Lazer - R$ 150

Produtos disponíveis para explicar:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- Tesouro IPCA+ (risco médio)
- CRI/CRA (risco médio)
...

```
