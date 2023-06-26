from flask import Flask

app = Flask(__name__)


def homepage():
    return 'Essa é minha HomePage'


app.run()
