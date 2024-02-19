from flask import Flask
import requests
from datetime import date

app = Flask(__name__)

# Members API Route
@app.route('/members')
def members():
    return {"members": ["Member1", "Member2", "Member3", "Member4", "Member5"]}

@app.route('/news')
def news():

    todayDate = date.today()
    weekAgoDate = todayDate.replace(day=todayDate.day-7)

    url = ('https://newsapi.org/v2/everything?'
           'q=IT&'
            'sortBy=relevancy&'
            'from=' + str(weekAgoDate) + '&'
            'to=' + str(todayDate) + '&'
            'apiKey=8fb05a75535a4174b04a5fab022be346'
            )
    response = requests.get(url)
    articles = response.json().get('articles')[:15]

    return articles


if __name__ == "__main__":
    app.run(debug=True)
