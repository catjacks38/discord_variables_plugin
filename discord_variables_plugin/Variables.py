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
        # If there was an error, the function will return -1
        try:
            return pickle.loads(base64.b64decode(self.varDict[str(server.id)][var]))
        except:
            return -1

    def clearServer(self, server: discord.Guild):
        # Clears all of the variables from the server.id dictionary
        # Returns -1 if there was an error
        try:
            del self.varDict[str(server.id)]
        except:
            return -1

    def removeVar(self, server: discord.Guild, var: str):
        # Removes var from the server.id dictionary
        # Returns -1 if there was an error
        try:
            del self.varDict[str(server.id)][var]
        except:
            return -1

    def save(self, fp: str):
        # Saves self.varDict in JSON format to fp
        # Returns -1 if there was an error
        try:
            with open(fp, "w") as file:
                json.dump(self.varDict, file)
        except:
            return -1

    def load(self, fp: str):
        # Loads fp into self.varDict
        # Returns -1 if there was an error
        try:
            with open(fp, "r") as file:
                self.varDict = json.load(file)
        except:
            return -1


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
        # If there was an error, the function will return -1
        try:
            return pickle.loads(base64.b64decode(self.varDict[str(user.id)][var]))
        except:
            return -1

    def clearUser(self, user: discord.User):
        # Clears all of the variables from the user.id dictionary
        # Returns -1 if there was an error
        try:
            del self.varDict[str(user.id)]
        except:
            return -1

    def removeVar(self, user: discord.User, var: str):
        # Removes var from the user.id dictionary
        # Returns -1 if there was an error
        try:
            del self.varDict[str(user.id)][var]
        except:
            return -1

    def save(self, fp: str):
        # Saves self.varDict in JSON format to fp
        # Returns -1 if there was an error
        try:
            with open(fp, "w") as file:
                json.dump(self.varDict, file)
        except:
            return -1

    def load(self, fp: str):
        # Loads fp into self.varDict
        # Returns -1 if there was an error
        try:
            with open(fp, "r") as file:
                self.varDict = json.load(file)
        except:
            return -1
