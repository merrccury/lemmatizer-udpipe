from lemmatizer import tag_ud
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/lemmatize', methods=['POST'])
def lemmatize():
    body = request.json
    text = body['data']
    tokens = tag_ud(text=text)
    response = {
        'lemms': tokens
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
