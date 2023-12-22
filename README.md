Análise de Sentimentos no Twitter com Python e spaCy

Este projeto visa realizar uma análise de sentimentos no Twitter utilizando Python, a API do Twitter, e a biblioteca spaCy para pré-processamento avançado de texto. 
A análise proporciona insights sobre as tendências de sentimentos em relação a um tópico específico.

Conteúdo do Projeto

    Configuração:
        Configure suas chaves de API do Twitter no script.
        Instale as bibliotecas necessárias executando pip install tweepy textblob matplotlib seaborn spacy no seu ambiente virtual.

Obtenção de Tweets:

    Utilizamos a API do Twitter para buscar tweets relacionados a um tópico específico.

Pré-processamento de Texto:

    Utilizamos spaCy para realizar a lematização e remover stop words, melhorando a qualidade da análise de sentimentos.

Análise de Sentimentos:

    A biblioteca TextBlob é empregada para avaliar a polaridade dos tweets.

Análise Temporal:

    Integramos as datas dos tweets para realizar uma análise temporal da polaridade dos sentimentos.

Visualização Gráfica:

    Utilizamos Matplotlib e Seaborn para criar visualizações gráficas, como um histograma da distribuição de polaridades ao longo do tempo.

Execução do Projeto

Para executar o projeto, siga os passos descritos na seção "Configuração" e, em seguida, execute o script. Certifique-se de ter as permissões necessárias da API do Twitter.

python twitter_sentiment_analysis.py

