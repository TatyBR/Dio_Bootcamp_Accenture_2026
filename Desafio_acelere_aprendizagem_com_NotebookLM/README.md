
# 📚 Guia de Estudos em Engenharia de Dados: do básico à criação de projetos iniciais

Este repositório foi criado como resposta ao **Desafio: Acelere sua Aprendizagem com IA: Explore o Poder do NotebookLM** do **Módulo:** IA para acelerar o desenvolvimento do **Bootcamp Dio Accenture** - Python para Análise e Automação de Dados. Aqui descrevemos como criamos um **Guia de Estudos em Engenharia de Dados** utilizando o NotebookLM.

O NotebookLM é uma IA que atua como um especialista exclusivo sobre determinado assunto. O assunto é definido pelos materiais que fornecemos a ela, como PDFs, vídeos, artigos, ou por aquilo que ela mesmo pesquisa na Web de acordo com o que é definido/ orientado,  evitando alucinações ou respostas fora de contexto.

---

## 🎯 Contexto e Objetivos

A Engenharia de Dados é uma das áreas mais estratégicas do mercado de tecnologia atual, sendo responsável por construir e manter diversos projetos, que tornam dados acessíveis e utilizáveis para análises e decisões de negócio.

Este caderno temático foi criado com o objetivo de:
- Orientar os estudos de quem deseja atuar na área de Engenharia de Dados;
- Consolidar os fundamentos teóricos e práticos da Engenharia de Dados;
- Organizar uma curadoria de fontes confiáveis e acessíveis sobre o tema;
- Documentar todo o processo de aprendizado;
- Gerar um Guia Completo que também pode ser reutilizável para revisões futuras.

---

## 📁 Curadoria de Fontes

Com base no vasto conteúdo das fontes, foram 36 no total, destacamos abaixo aquelas que mais oferecem uma base sólida e abrangente no o aprendizado da Engenharia de Dados:

### 📖 Livro: Fundamentos de Engenharia de Dados (Joe Reis & Matt Housley)
Esta é considerada a obra definitiva para a área, pois não foca apenas em ferramentas, mas nos princípios que resistem ao tempo. Ela introduz o conceito do **Ciclo de Vida da Engenharia de Dados**, composto por cinco etapas: geração, armazenamento, ingestão, transformação e disponibilização. Além disso, destaca seis elementos subjacentes que devem permear todo o projeto: segurança, gerenciamento de dados, DataOps, arquitetura, orquestração e engenharia de software.

### 📖 Dissertação: Ensino de Engenharia de Dados nas Universidades Brasileiras (UFAM)
Este documento identifica a lacuna entre o que é ensinado na academia (focado em bancos relacionais) e o que o mercado exige (Big Data, Nuvem e Processamento Distribuído). A fonte é valiosa por propor uma **nova ementa de disciplina** que equilibra teoria e prática, incluindo tópicos como Bancos NoSQL, técnicas de *Change Data Capture* (CDC) e formatos de arquivos modernos (Parquet, Avro).
(https://tede.ufam.edu.br/bitstream/tede/10835/6/DISS_TarsisAzevedo_PPGI.pdf)

### 📕 Guia Compacto: Engenharia de Dados na Databricks (PDF)
Foca na modernização da área através da **Plataforma de Inteligência de Dados** e da arquitetura **Data Lakehouse**. Apresenta ferramentas específicas para unificar o fluxo de trabalho, como o *Lakeflow* (para ingestão e transformação) e o *Unity Catalog* (para governança). É essencial para entender como empresas líderes utilizam a nuvem para escalar IA e BI.

### 📕 Arquitetura Medalhão: O Guia Definitivo (Data Science Academy)
Explica o padrão de design mais popular para organizar um Data Lakehouse, dividindo-o em três camadas lógicas: **Bronze** (dados brutos), **Prata** (dados filtrados e limpos) e **Ouro** (dados agregados prontos para o negócio). O resumo destaca as vantagens de rastreabilidade e reprodutibilidade dos dados ao adotar este modelo.
(https://blog.dsacademy.com.br/arquitetura-medalhao-o-guia-definitivo-para-organizar-o-data-lakehouse-fundamentos/)

### 📕 Comparativo IBM: Data Warehouses vs. Data Lakes vs. Data Lakehouses
Fornece uma distinção teórica clara entre os modelos de armazenamento. Enquanto o *Data Warehouse* foca em dados estruturados e consultas rápidas, e o *Data Lake* armazena dados brutos de forma barata, o **Data Lakehouse** surge como a convergência que une o desempenho do primeiro com a flexibilidade do segundo.
(https://www.ibm.com/br-pt/think/topics/data-warehouse-vs-data-lake-vs-data-lakehouse)

### 📚 Roadmap Engenharia de Dados 2026 (Matheus Domingos)
Oferece uma visão atualizada das competências necessárias, destacando o **Python** como a linguagem mais popular e o **SQL** como indispensável para transformações rotineiras. Sugere uma trilha que passa por orquestração (Airflow), processamento distribuído (Spark) e ferramentas de modelagem moderna como o **dbt**.
(https://matheusdomingos.substack.com/p/roadmap-engenharia-de-dados-2026)

### 🖥️ Repositório: "Open the Gate" Data Engineering (GitHub)
Uma fonte comunitária que organiza uma trilha progressiva de aprendizado gratuito. O diferencial é a separação por módulos, começando pelos fundamentos (OLTP vs. OLAP), passando por pipelines (ETL vs. ELT) até chegar em projetos práticos que podem ser rodados localmente usando **Docker** e **DuckDB**.
(https://github.com/IgorTiburcio81/open-the-gate-data-engineering)

### 🖥️ Vídeo: As maiores dúvidas sobre Engenharia de Dados (vbluuiza)
Foca nas *hard skills* e na transição de carreira, reforçando que a Engenharia de Dados é um subdomínio da **Engenharia de Software**. Luíza destaca a importância de estudar não apenas ferramentas, mas fundamentos como o SOLID, engenharia de requisitos e design de software para construir pipelines robustos.
(https://www.youtube.com/watch?v=jjTQwuZDdT4)

### 🖥️ Aula 1: Introdução à Engenharia de Dados (Canal Engenharia de Dados)
Define o papel do engenheiro como o criador de "canos" que transformam dados em informação. Introduz conceitos fundamentais sobre a execução de pipelines, diferenciando o processamento em **Batch** (em lotes, agendado) do processamento em **Streaming** (tempo real), dependendo da necessidade do negócio.
(https://www.youtube.com/watch?v=pQtG3ByDoEM)


✔️Além das fontes fornecidas, foi inserido um texto para definir uma identidade ao NotebookLM: "Você é um especialista em Engenharia de Dados mas ama atuar como orientar/professor desta área".


✔️Também foi pedido ao NotebookLM que ele realiza-se uma pesquisa na Web, seguindo o tema: Fundamentos teóricos e como iniciar na prática da Engenharia de Dados
 


## 🧪 Engenharia de Prompts

Os prompts foram elaborados de maneira que o NotebookLM usa-se sempre as fontes existentes e trouxe-se as respostas seguindo as orientações de como elas deveriam vir elaboradas. 


### Prompt 1 - Resumo sobre o assunto:
```
Com base em todas as fontes carregadas:
Crie um resumo estruturado sobre Engenharia de Dados cobrindo:

O que é e qual o papel do Engenheiro de Dados hoje?

1. Quais são os principais pontos teóricos/ conceitos que devam ser estudados antes da criação de projetos?
2. Quais os principais projetos de Engenharia de Dados são citados nas fontes?
3. Considerando os projetos descritos, quais as principais etapas deles?
4. Quais as ferramentas mais citadas nas fontes.

Use uma linguagem clara e acessível para iniciantes e organize com títulos e tópicos.
```

### Prompt 2 - Roteiro de estudos separado por semanas:
```
Com base nas fontes fornecidas, crie um roteiro de estudos de 8 semanas para um iniciante absoluto em Engenharia de Dados, seguindo esta estrutura para cada semana:

- Tema principal.
- Conceitos a estudar.
- Ferramentas para conhecer.
- Atividades práticas sugeridas.
- Recurso da fonte que cobre esse conteúdo.

O roteiro deve evoluir do mais conceitual (semana 1) para o mais prático (semana 8).
```

### Prompt 3 - Sugestão de projetos que possam ser confeccionados:
```
Com base nas ferramentas e conceitos mencionados nas fontes, sugira 3 projetos práticos que possam ser confeccionados por iniciantes em Engenharia de Dados com:

- Nome do projeto.
- Objetivo.
- Ferramentas necessárias (gratuitas).
- Dados públicos que podem ser usados.
- Nível de complexidade (fácil / médio).
- O que esse projeto demonstra para um recrutador.
```

## 💡 Caderno gerado pelo NotebookLM

Para consulta das respostas e de todo caderno gerado segue o link:
https://notebooklm.google.com/notebook/53c65277-73d4-4937-9a27-c3b1f04e1078


### 🔁 Prompts Reutilizáveis para Revisão Futura

Os prompts abaixo poderão ser utilizados em qualquer sessão futura do NotebookLM, visando aprofundar os estudos em Engenharia de Dados:

```text
1. "Crie 10 perguntas de revisão levando em consideração o que foi estudado no roteiro de estudos elaborado anteriormente."

2. "Liste os erros mais comuns de iniciantes ao implementar projetos e como evitá-los."

3. "Quais os processos passos a seguir para aprofundar mais os meus estudos para um nível avançado? Crie um novo guia de estudos neste sentido"

5. "Dado que já finalizei os projetos iniciais me traga agora sugestão de projetos mais avançados."
```




## 👩‍💻 Autora:

🎯 Feito com dedicação e muito aprendizado por **Taíta B. Ramos**.