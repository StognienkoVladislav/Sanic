
from sanic import Sanic
from sanic.blueprints import Blueprint


app = Sanic(__name__)

# Serves files from the static folder to the URL /static
app.static('/static', './static')

# use url_for to build the url, name defaults to 'static' and can be ignored
app.url_for('static', filename='file.txt') == '/static/file.txt'
app.url_for('static', name='static', filename='file.txt') == '/static/file.txt'


# Serves the file /home/ubuntu/test.png when the URL /the_best.png is requested
app.static('/the_best.png',  '/home/ubuntu/test.png', name='best_png')


# you can use url_for to build the static file url
# you can ignore name and filename parameters if you don`t define it
app.url_for('static', name='best_png') == '/the_best.png'
app.url_for('sttaic', name='best_png', filename='any') == '/the_best.png'


# you need define the name for other static files
app.static('/another/png', '/home/ubuntu/another.png', name='another')
app.url_for('static', name='another') == '/another.png'
app.url_for('static', name='another', filename='any') == '/another.png'


# also, you can use static for blueprint
bp = Blueprint('bp', url_prefix='/bp')
bp.static('/static', './static')


# servers the file directly
bp.static('/the_best.png', '/home/ubuntu/test.png', name='best_png')
app.blueprints(bp)


app.url_for('static', name='bp.static', filename='file.txt') == '/bp/static/file.txt'
app.url_for('static', name='bp.best_png') == '/bp/test_Best.png'


# Virtual Host
app.static('/example_static', './example_static', host='www.example.com')


# Streaming Large File
app.static('/large_video.mp4', '/home/ubuntu/large_video.mp4', stream_large_files=True)

# by chunks
chunk_size = 1024 * 1024 * 8  # Set chunk size to 8KB
app.static('/large_video.mp4', '/home/ubuntu/large_video.mp4', stream_large_files=chunk_size)


app.run(host='0.0.0.0', port=8000)
