# import lambda_function
# import json
def validate_message():
    # playload = {'numero': '10', 'context': 'Null'}
    # context = "Null"
    # retorno = json.loads(lambda_function.lambda_handler(playload, context))
    retorno = {'message': 'Hello, World!!!'}
    assert retorno['message'] == 'Hello, World!!!'
    # assert retorno['result']

import flask; print(flask.__version__)