# 🔍 Detecção de Fraudes em Transações de Cartão de Crédito

Este projeto foi criado visando o estudo prático de algumas técnicas de Machine Learning aplicadas à detecção de fraudes financeiras. O notebook explora o uso de alguns modelos simples até algoritmos avançados, passando por técnicas de balanceamento de dados e interpretabilidade de modelos.

---

## 📚 Objetivo

Estudar e comparar diferentes algoritmos e técnicas de ML para identificar transações fraudulentas em um dataset altamente desbalanceado, entendendo as métricas, limitações e boas práticas de cada abordagem.

---

## 🗂️ Conhecendo o Dataset: creditcard.csv

O Dataset escolhido para estudo foi o **creditcard.csv** que é um famoso conjunto de dados usado globalmente por estudantes e pesquisadores para treinar algoritmos focados na detecção de fraudes. Ele contém transações financeiras reais realizadas por cartões de crédito europeus no decorrer do ano de 2013 e tem a seguinte estrutura:

| Colunas    | Descrição                                                                    |
|------------|------------------------------------------------------------------------------|
| Time       | Segundos decorridos entre cada transação e a primeira transação registrada   | 
| V1 a V28   | Variáveis anonimizadas via PCA (Análise de Componentes Principais) por questões de privacidade.                                               | 
| Amount     | Valor monetário da transação em € (EURO)                                     | 
| Class      | 0 = transação legítima (normal) / 1 = fraude                                 | 

Uma das características principais deste Dataset é que ele é **altamente desbalanceado**, pois menos de **0,17%** dos registros são fraudes, o que exige técnicas especiais para treinamento dos modelos sem que eles apenas "adivinhem" tudo como transação normal.


**Fonte:** [`creditcard.csv`](https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv) — disponibilizado pelo Google/TensorFlow (originalmente do Kaggle).

---

## 🧪 Técnicas e Modelos Estudados

### Pré-processamento e Feature Engineering
- Transformação logarítmica em `Amount` com `np.log1p` para comprimir a escala dos valores financeiros.
- Padronização com `StandardScaler` (média 0, desvio padrão 1).
- Divisão treino/teste com `stratify` para preservar a proporção das classes.

### Tratando o Desbalanceamento
| Técnica | Descrição | Recall obtido |
|---|---|---|
| Sem balanceamento | Dataset original | 0.67 ⚠️ |
| **Undersampling** | Reduz a classe majoritária | 0.93 ✅ |
| **Oversampling (SMOTE)** | Gera exemplos sintéticos da classe minoritária | 0.97 ✅ |

### Modelos
| Modelo | Precision (fraude) | Recall (fraude) | Observação |
|---|---|---|---|
| Regressão Logística | 0.85 | 0.67 | Baseline — simples e interpretável |
| Regressão Logística + Undersampling | 0.95 | 0.93 | Melhora o recall, mas tem perda de dados |
| Regressão Logística + SMOTE | 0.99 | 0.97 | Melhora o equilíbrio, mas gera dados artificiais |
| Random Forest | 0.84 | 0.76 | Árvores de Decisão - Lida melhor com dados desbalanceados |
| **XGBoost** | **0.93** | **0.78** | Melhor modelo — boosting sequencial |

---

## 📊 Métricas Utilizadas

- **Acurácia**: útil, mas enganosa em datasets desbalanceados.
- **Precision**: das transações classificadas como fraude, quantas realmente são?
- **Recall**: das fraudes reais, quantas o modelo detectou?
- **F1-Score**: média harmônica entre Precision e Recall.
- **Curva ROC / AUC**: capacidade do modelo separar fraude de transação normal.
- **Curva Precision-Recall**: métrica mais adequada para datasets desbalanceados.

---

## ⚙️ Outros Conceitos Estudados

- **Pipeline** com Scikit-learn para organizar o fluxo de pré-processamento + modelo.
- **Ajuste de threshold**: alterando o limiar de 0.5 para 0.3 para aumentar a sensibilidade do modelo a fraudes.
- **Ajuste de Hiperparâmetros** com `GridSearchCV` (testando `max_depth` e `n_estimators` no XGBoost).
- **Explicabilidade com SHAP**: visualização de como cada feature influencia na decisão do modelo XGBoost.
- **Visualização de Árvores** do Random Forest com `plot_tree`.

---

## 🛠️ Bibliotecas Utilizadas

```python
pandas, numpy, matplotlib
scikit-learn  # modelos, métricas, pipeline, GridSearchCV
imbalanced-learn (imblearn)  # SMOTE
xgboost  # XGBClassifier
shap  # explicabilidade
dtreeviz  # visualização de árvores
```

---

## 💡 Principais Aprendizados

- Em problemas desbalanceados a **acurácia não é a métrica mais acertiva**, então o mais recomendável é priorizar a Recall e F1-Score para a classe minoritária.
- **SMOTE** superou Undersampling por não descartar dados da classe majoritária.
- **XGBoost** apresentou os melhores resultados gerais entre os modelos testados.
- **SHAP** é uma ferramenta poderosa para entender o "porquê" das decisões do modelo.
- Ajustar o **threshold** é uma alternativa simples para melhorar o Recall sem retreinar o modelo.

---


> 📌 *Este projeto foi desenvolvido apenas para fins exclusivamente educacionais, visando o estudo de técnicas de Machine Learning aplicadas a detecção de fraudes. Foi desenvolvido para a conclusão do **módulo Python aplicado à Análise** do **Bootcamp Dio Accenture 2026***


👩‍💻 Autora:
--- 
🎯 Feito com dedicação e muito aprendizado por Taíta B. Ramos.
