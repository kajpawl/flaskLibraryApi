from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    # print(f'headers: {request.headers}')
    # print(f'method: {request.method}')
    # print(f'path: {request.path}')
    # print(f'url: {request.url}')

    print('Authorization header: ' + request.headers['Authorization'])
    print('Request content type: ', request.headers['Content-type'])
    print('Request body: ', request.json)
    print('Single key in request body: ', request.json['age'])
    print('Single key in request body - with get method: ', request.json.get('name'))

    return 'Hello from Flask!'


if __name__ == '__main__':
    app.run(debug=True)
