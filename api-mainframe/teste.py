import json
# import data
from data import Data

# class Data:
#     Result = None
#     Terminal = None
#     Server = None
#     # def __init__(self):
#     # self.Result = Result
#     # self.Terminal = Terminal
#     # self.Server = Server

def mainframe():
    # x = data.Data()
    x = Data()
    x.Result = "result"
    x.Terminal = "terminal"
    x.Server = "server"
    return json.dumps(x.__dict__)

if __name__ == '__main__':
    print(mainframe())
