import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
from datetime import datetime

# Chaves de API do Twitter
consumer_key = 'sua_consumer_key'
consumer_secret = 'seu_consumer_secret'
access_token = 'seu_access_token'
access_token_secret = 'seu_access_token_secret'

# Autenticação
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Carregar o modelo spaCy para o idioma português
nlp = spacy.load('pt_core_news_sm')

def obter_tweets(query, quantidade=100):
    try:
        # Pesquisa por um tópico específico
        public_tweets = tweepy.Cursor(api.search, q=query, lang='pt').items(quantidade)
        return [(tweet.text, tweet.created_at) for tweet in public_tweets]

    except tweepy.TweepError as e:
        print(f"Erro na obtenção de tweets: {e}")
        return []

def preprocessamento(texto):
    doc = nlp(texto)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return ' '.join(tokens)

def analisar_sentimentos(tweets):
    polaridades = []
    for tweet, _ in tweets:
        texto_preprocessado = preprocessamento(tweet)
        analysis = TextBlob(texto_preprocessado)
        polaridades.append((texto_preprocessado, analysis.sentiment.polarity))
    return polaridades

def visualizar_sentimentos(polaridades, datas):
    sns.set()
    plt.figure(figsize=(12, 8))
    for i in range(len(polaridades)):
        plt.scatter(datas[i], polaridades[i][1], color='skyblue')
    plt.title('Análise Temporal de Sentimentos')
    plt.xlabel('Data')
    plt.ylabel('Polaridade')
    plt.show()

def main():
    # Parâmetros
    topico_pesquisa = 'Python'
    quantidade_tweets = 200

    # Obtendo tweets
    tweets = obter_tweets(topico_pesquisa, quantidade_tweets)

    if not tweets:
        print("Nenhum tweet encontrado. Encerrando o programa.")
        return

    # Separando tweets e datas
    textos, datas = zip(*tweets)

    # Analisando sentimentos
    polaridades = analisar_sentimentos(tweets)

    # Visualizando resultados
    visualizar_sentimentos(polaridades, datas)

if __name__ == "__main__":
    main()
