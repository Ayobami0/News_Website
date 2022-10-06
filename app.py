from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = 'a295922be4ab4e4b9e4c9b83e57c02d5'
NEWS_TYPE = ['everything', 'top-headlines']
URL = 'https://newsapi.org/v2/'
COUNTRY = 'us'


def data(news_type, country='ng', q='', page_size=10, lang='en', page=1):
    news_map = {}
    if news_type == 'top-headlines':
        response = requests.get(f'{URL}{news_type}?country={country}&apiKey={API_KEY}')
        for value, item in enumerate(response.json()['articles'], 1):
            news_map[value] = item
        return news_map
    elif news_type == 'everything':
        response = requests.get(f'{URL}{news_type}?q={q}&pageSize={page_size}&page={page}&language={lang}&apiKey={API_KEY}')
        total_page = response.json()['totalResults']//page_size
        for value, item in enumerate(response.json()['articles'], 1):
            news_map[value] = item
        return (news_map, total_page)


@app.route('/')
def home():
    return render_template('index.html', news=data(NEWS_TYPE[1]))


@app.route('/<genre>', defaults={'page': 1})
@app.route('/<genre>/<int:page>')
def query(genre=None, page=None):
    # return render_template('newsPage.html')
    news = data(NEWS_TYPE[0], q=genre)[0]
    total_page = data(NEWS_TYPE[0], q=genre)[1]
    print(total_page)
    return render_template('pages/genre.html', page=page, news=news, totalPage=total_page)


if __name__ == 'main':
    app.run()
