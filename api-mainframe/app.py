from flask import Flask
import json
from data import Data
app = Flask(__name__)


# class Data():
#     Result="result"
#     Terminal="terminal"
#     Server="server"

@app.route('/', methods=['POST', 'GET'])
def mainframe():
    # criando a instancia do objeto
    x = Data()
    x.Result = "result"
    x.Terminal = "terminal"
    x.Server = "server"

    return json.dumps(x.__dict__)

if __name__ == '__main__':
    app.run()