from flask import Flask, request, make_response, jsonify


app = Flask(__name__)


@app.route('/')
def index():
    # print(f'headers: {request.headers}')
    # print(f'method: {request.method}')
    # print(f'path: {request.path}')
    # print(f'url: {request.url}')

    # print('Authorization header: ' + request.headers['Authorization'])
    # print('Request content type: ', request.headers['Content-Type'])
    # print('Request body: ', request.json)
    # print('Single key in request body: ', request.json['age'])
    # print('Single key in request body - with get method: ', request.json.get('name'))

    # html_response = '<h1>Hello from Flask!</h1>'
    # response = make_response([{'id': 1, 'title': 'Title'}], 200)  # code 200 is returned by default - can be skipped
    # response.headers['Content-Type'] = 'application/json'
    response = jsonify([{'id': 1, 'title': 'Title'}])
    response.status_code = 201

    return response


if __name__ == '__main__':
    app.run(debug=True)
