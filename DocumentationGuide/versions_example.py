
from sanic import Sanic
from sanic import response


app = Sanic(__name__)


@app.route('/text', version=1)
def handle_request(request):
    return response.text('Hello world! Version 1')


@app.route('/text', version=2)
def handle_request(request):
    return response.text('Hello world! Version 2')


app.run()
