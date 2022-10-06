from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'a295922be4ab4e4b9e4c9b83e57c02d5'
NEWS_TYPE = ['everything', 'top-headlines']
URL = 'https://newsapi.org/v2/'
COUNTRY = 'us'


def data(news_type, country):
    return requests.get(f'{URL}{news_type}?country={country}&apiKey={API_KEY}')


response = data(NEWS_TYPE[1], COUNTRY).json()

news_map = {}

for value, item in enumerate(response['articles'], 1):
    news_map[value] = item

for key, value in news_map.items():
    print(value['source'])


@app.route('/')
def home():
    return render_template('index.html', news=news_map)


@app.route('/NEWS/<source>')
def content(source):
    # return render_template('newsPage.html')
    return f'<p>{news_map.get(int(source))["content"]}</p>'


if __name__ == 'main':
    app.run()
