import json
import pickle
import base64
import discord


# A class to store servers specific variables
class ServerVariables:
    varDict = {}

    def set(self, server: discord.Guild, var: str, obj):
        # Tries to write to var key of the server.id dictionary
        # If there is does not exist, a new var key will be created
        try:
            self.varDict[str(server.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")
        except:
            self.varDict[str(server.id)] = {}
            self.varDict[str(server.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")

    def get(self, server: discord.Guild, var: str):
        # Tries to read the var key of the server.id dictionary
        return pickle.loads(base64.b64decode(self.varDict[str(server.id)][var]))

    def clearServer(self, server: discord.Guild):
        # Clears all of the variables from the server.id dictionary
        del self.varDict[str(server.id)]

    def removeVar(self, server: discord.Guild, var: str):
        # Removes var from the server.id dictionary
        del self.varDict[str(server.id)][var]

    def save(self, fp: str):
        # Saves self.varDict in JSON format to fp
        with open(fp, "w") as file:
            json.dump(self.varDict, file)

    def load(self, fp: str):
        # Loads fp into self.varDict
        with open(fp, "r") as file:
            self.varDict = json.load(file)


# A class to store global user variables
class GlobalUserVariables:
    varDict = {}

    def set(self, user: discord.User, var: str, obj):
        # Tries to write to var key of the user.id dictionary
        # If there is does not exist, a new var key will be created
        try:
            self.varDict[str(user.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")
        except:
            self.varDict[str(user.id)] = {}
            self.varDict[str(user.id)][var] = base64.b64encode(pickle.dumps(obj)).decode("utf-8")

    def get(self, user: discord.User, var: str):
        # Tries to read the var key of the user.id dictionary
        return pickle.loads(base64.b64decode(self.varDict[str(user.id)][var]))

    def clearUser(self, user: discord.User):
        # Clears all of the variables from the user.id dictionary
        del self.varDict[str(user.id)]

    def removeVar(self, user: discord.User, var: str):
        # Removes var from the user.id dictionary
        del self.varDict[str(user.id)][var]

    def save(self, fp: str):
        # Saves self.varDict in JSON format to fp
        with open(fp, "w") as file:
            json.dump(self.varDict, file)

    def load(self, fp: str):
        # Loads fp into self.varDict
        with open(fp, "r") as file:
            self.varDict = json.load(file)
