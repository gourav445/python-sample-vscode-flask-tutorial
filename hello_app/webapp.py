# Entry point for the application.
from . import app    # For application discovery by the 'flask' command. 
from . import views  # For import side-effects of setting up routes. 

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()

# Time-saver: output a URL to the VS Code terminal so you can easily Ctrl+click to open a browser
# print('http://127.0.0.1:5000/hello/VSCode')
