
from sanic import Sanic
from my_blueprint import bp, blueprint_v1, blueprint_v2


app = Sanic(__name__)
app.blueprint(bp)
app.blueprint(blueprint_v1)
app.blueprint(blueprint_v2)

app.run(host='0.0.0.0', port=8000, debug=True)
