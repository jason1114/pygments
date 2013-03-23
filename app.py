import os
from flask import Flask
from flask import request
from flask import Response
from flask import render_template
from flask import Markup

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import logging, sys
logging.basicConfig(stream=sys.stderr)
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        content = Markup(markdown.markdown(open('README.md', 'r').read()))
        return render_template('index.html', **locals())
    elif request.method == 'POST':
        return pygmentize(request.form["lang"], request.form["code"])

@app.route('/default.css')
def css():
    return Response(open('default.css', 'r').read(), mimetype = 'text/css')

def pygmentize(lang, code):
  lexer     = get_lexer_by_name(lang)
  formatter = HtmlFormatter()
  return highlight(code, lexer, formatter)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port)
