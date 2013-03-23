import os
from flask import Flask
from flask import request

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import logging, sys
logging.basicConfig(stream=sys.stderr)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return open('README', 'r').read()
    elif request.method == 'POST':
        return pygmentize(request.form("lang"), request.form("code"))

def pygmentize(lang, code):
  lexer     = get_lexer_by_name(lang)
  formatter = HtmlFormatter()
  return highlight(code, lexer, formatter)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
