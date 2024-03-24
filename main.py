from flask import Flask, jsonify, request

app = Flask(__name__)

import csv

all_articles = []
liked_articles = []
not_liked_articles = []

with open('path/to/articles.csv', 'r') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  
    headers[0] = 'id'  
    for row in csv_reader:
        all_articles.append(dict(zip(headers, row)))

@app.route('/get_article', methods=['GET'])
def get_article():
    return jsonify(all_articles[0])

@app.route('/like_article', methods=['POST'])
def like_article():
    article = all_articles.pop(0)
    liked_articles.append(article)
    return jsonify({'success': True})

@app.route('/not_like_article', methods=['POST'])
def not_like_article():
    article = all_articles.pop(0)
    not_liked_articles.append(article)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
