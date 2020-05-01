from flask import Flask
from flask import render_template

# The secon parameter is optional. It allows to set the static folder accessible via the root URL instead of via /static/foo
app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def home():    
    return render_template('layout.html', title="Give me a game", content_title="Hall of fames")