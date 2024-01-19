#from flask import Flask
#from markupsafe import escape

#app = Flask(__name__)


#@app.route('/')
#@app.route("/<name>")
#def hello(name=None):
#    return f"Hello, {escape(name)}!"

#New code from Step 1.4
from flask import current_app as app


@app.route('/')
def hello():
  return f"Hello!"