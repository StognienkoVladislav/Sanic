
from sanic import Sanic
from sanic.log import logger
from sanic.response import json, text


app = Sanic('test')


@app.route('/')
async def test(request):
    logger.info('Here is your log')
    return text('Hello world')


@app.route('/json')
async def post_json(request):
    return json({'received': True, 'message': request.json})


@app.route('/query_string')
async def query_string(request):
    return json({'parsed': True, 'args': request.args, 'url': request.url,
                 'query_string': request.query_string})


@app.route("/test_request_args")
async def test_request_args(request):
    return json({
        "parsed": True,
        "url": request.url,
        "query_string": request.query_string,
        "args": request.args,
        "raw_args": request.raw_args,
        "query_args": request.args,
    })


@app.route('/files')
async def post_json(request):
    test_file = request.files.get('test')

    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type
    }

    return json({
        'received': True,
        'file_names': request.files.keys(),
        'test_file_parameters': file_parameters
    })


@app.route('/form')
async def post_form_json(requst):
    return json({'received': True, 'form_data': requst.form, 'test': requst.form.get('test')})


@app.route('/users', methods=['POST',])
def create_user(request):
    return text('You are trying to create a user with the following POST: {}'.format(request.body))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
