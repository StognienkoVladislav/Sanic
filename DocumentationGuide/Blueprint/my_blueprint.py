
from sanic import Blueprint
from sanic.response import json, text, redirect

bp = Blueprint('my_blueprint')


@bp.listener('before_server_start')
async def setup_connection(app, loop):
    global database
    # database = mysql.connect(host='127.0.0.1'...)


@bp.listener('after_server_stop')
async def close_connection(app, loop):
    await database.close()


@bp.route('/')
async def bp_root(request):
    return json({'my': 'blueprint'})


blueprint_v1 = Blueprint('v1', url_prefix='/api', version="v1")
blueprint_v2 = Blueprint('v2', url_prefix='/api', version="v2")


@blueprint_v1.route('/')
async def root(request):
    url = request.app.url_for('v1.post_handler', post_id=5)
    return redirect(url)


@blueprint_v1.route('/post/<post_id>')
async def post_handler(request, post_id):
    return text('Post {} in Blueprint V1'.format(post_id))


@blueprint_v2.route('/')
async def api_v2_root(request):
    return text('Welcome to version 2 of our documentation')
