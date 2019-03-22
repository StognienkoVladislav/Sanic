from sanic import Sanic
from sanic.response import json, text, redirect

app = Sanic('responses')


# Routing
@app.route('/')
async def test(request):
    return json({'hello': 'world'})


# Request parameters
@app.route('/tag/<tag>')
async def tag_handler(request, tag):
    return text('Tag - {}'.format(tag))


@app.route('/number/<integer_arg:int>')
async def integer_handler(request, integer_arg):
    return text('Integer - {}'.format(integer_arg))


@app.route('/number/<number_arg:number>')
async def number_handler(request, number_arg):
    return text('Number - {}'.format(number_arg))


@app.route('/person/<name:[A-z]+>')
async def person_handler(request, name):
    return text('Person - {}'.format(name))


@app.route('/folder/<folder_id:[A-z0-9]{0, 4}')
async def folder_handler(request, folder_id):
    return text('Folder - {}'.format(folder_id))


# Http request types
@app.route('/post', methods=['POST'])
async def post_handler(request):
    return text('Post request - {]'.format(request.json))


@app.route('/get', methods=['GET'], host='example.com')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))


# if the host header doesn't match example.com, this route will be used
@app.route('/get', methods=['GET'])
async def get_handler(request):
    return text('GET request in default - {}'.format(request.args))


# add_route method
async def handler1(requst):
    return text('OK')


async def handler2(request, name):
    return text('Folder - {}'.format(name))


async def person_handler_2(request, name):
    return text('Person - {}'.format(name))


# Add each handler function as a route
app.add_route(handler1, '/test')
app.add_route(handler2, '/folder/<name>')
app.add_route(person_handler_2, '/person/<name:[A-z]>', methods=['GET'])


# URL building with url_for
@app.route('/index')
async def index(request):
    # generate a URL for the endpoint post_handler
    url = app.url_for('post_handler', post_id=5)
    # the URl is '/post/5, redirect to it
    return redirect(url)


@app.route('/post/<post_id>')
async def post_handler(request, post_id):
    return text('Post - {}'.format(post_id))


# Websocket routes
@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'Hello'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
