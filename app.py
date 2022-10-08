from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)

API_KEY = 'a295922be4ab4e4b9e4c9b83e57c02d5'
NEWS_TYPE = ['everything', 'top-headlines']
URL = 'https://newsapi.org/v2/'
COUNTRY = 'us'


def data(news_type, country='ng', q='', page_size=10, lang='en', page=1):
    news_map = {}
    if news_type == 'top-headlines':
        response = requests.get(f'{URL}{news_type}?country={country}&apiKey={API_KEY}')
        print(response.json())
        for value, item in enumerate(response.json()['articles'], 1):
            news_map[value] = item
        return news_map
    elif news_type == 'everything':
        response = requests.get(f'{URL}{news_type}?q={q}&pageSize={page_size}&page={page}&language={lang}&apiKey={API_KEY}')
        print(response.json())
        total_page = 10
        for value, item in enumerate(response.json()['articles'], 1):
            news_map[value] = item
        return (news_map, total_page)


with open('dummy.json', 'r') as fp:
    file = json.load(fp)


@app.route('/')
def home():
    # return render_template('index.html', news=data(NEWS_TYPE[1]))
    return render_template(
            'index.html',
            news=file,
            latest=file
            )


# @app.route('/<genre>', defaults={'page': 1})
@app.route('/<genre>/<int:page>', methods=['GET', 'POST'])
def query(genre, page):
    if request.method == 'POST':
        page = int(request.form['page-no'])
        return redirect(url_for('query', genre=genre, page=page))
    # return render_template('newsPage.html')
    print(page)
    news_data = data(NEWS_TYPE[0], q=genre, page=page)
    return render_template(
            'pages/genre.html',
            page=page,
            genre=genre,
            latest=file,
            news=news_data[0],
            totalPage=news_data[1],
            )


if __name__ == 'main':
    app.run()
