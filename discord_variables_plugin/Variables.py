import json
import pickle
import base64


class ServerVariables:
    varDict = {}

    def set(self, server, var, obj):
        try:
            self.varDict[str(server.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")
        except:
            self.varDict[str(server.id)] = {}
            self.varDict[str(server.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")

    def get(self, server, var):
        try:
            return pickle.loads(base64.b64decode(self.varDict[str(server.id)][var]))
        except:
            return -1

    def removeServer(self, server):
        try:
            del self.varDict[str(server.id)]
        except:
            return -1

    def removeVar(self, server, var):
        try:
            del self.varDict[str(server.id)][var]
        except:
            return -1

    def save(self, fp):
        try:
            with open(fp, "w") as file:
                json.dump(self.varDict, file)
        except:
            return -1

    def load(self, fp):
        try:
            with open(fp, "r") as file:
                self.varDict = json.load(file)
        except:
            return -1
