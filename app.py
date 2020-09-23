from flask import Flask, request, make_response, jsonify

POSTS = [
    {
        'id': 1,
        'title': 'title 1',
        'text': 'text 1'
    },
    {
        'id': 2,
        'title': 'title 2',
        'text': 'text 2'
    },
    {
        'id': 3,
        'title': 'title 3',
        'text': 'text 3'
    },
    {
        'id': 4,
        'title': 'title 4',
        'text': 'text 4'
    }
]

app = Flask(__name__)


@app.route('/posts')
def items():
    response_data = {
        'success': True,
        'data': POSTS
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
