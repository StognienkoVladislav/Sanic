
from sanic import Sanic
from sanic.response import text

app = Sanic('cookies')


# Reading cookies
@app.route('/get_cookie')
async def test(request):
    test_cookie = request.cookies.get('test')
    return text('Test cookie set to: {}'.format(test_cookie))


# Writing cookies
@app.route('/set_cookie')
async def test(request):
    response = text('There`s a cookie up in this response')
    response.cookies['test'] = 'It worked!'
    response.cookies['test']['domain'] = 'gotta-go-fast.com'
    response.cookies['test']['httponly'] = True
    return response


# Deleting cookies
@app.route('/del_cookie')
async def test(request):
    response = text('Time to eat some cookie muhaha')

    # This cookie will be set to expire in 0`second
    del response.cookies['kill_me']

    # This cookie will self destruct in 5 seconds
    response.cookies['short_life'] = 'Glad to be here'
    response.cookies['short_life']['max-age'] = 5
    del response.cookies['favorite_color']

    # This cookie will remain unchanged
    response.cookies['favorite_color'] = 'blue'
    response.cookies['favorite_color'] = 'pink'
    del response.cookies['favorite_color']

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, access_log=True)
