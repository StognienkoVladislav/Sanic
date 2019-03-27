
from sanic import Sanic
from sanic.response import text
from sanic.exceptions import ServerError, abort

app = Sanic(__name__)


@app.route('/killme')
async def i_am_ready_to_die(request):
    raise ServerError('Something bad happend', status_code=500)


@app.route('/you_shall_not_pass')
async def no_no(request):
    abort(401)
    # this won`t happen
    text('OK')


if __name__ == '__main__':
    app.run()
