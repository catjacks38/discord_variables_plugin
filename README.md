# Discord Variables Plugin
## A plugin to help with saving variables for bots
## Instalation:
- Windows: `pip install discord_variables_plugins`
- Linux: `pip3 install discord_variables_plugins`
## Documentation:
### Server Specific Variables:
- Import package, and create discord_variables_plugin.ServerVariables object:
```python
import discord_variables_plugin
serverVars = discord_variables_plugin.ServerVariables()
```
- To set a server specific variable
```python
# Pass a discord.Guild object for guild
# Pass a string for varName
# Pass any object for value
serverVars.set(guild, varName, value)
```
- To get a server specific variable
```python
# Pass a discord.Guild object for guild
# Pass a string for varName
# Returns the object stored in varName of guild
varNameValue = serverVars.get(guild, varName)
```
- To clear a saved server
```python
# Pass a discord.Guild object for guild
serverVars.clearServer(guild)
```
- To remove a variable of a server
```python
# Pass a discord.Guild object for guild
# Pass a string for varName
serverVars.removeVar(guild, varName)
```
- To save the server variables
```python
# Pass a file path as fp
serverVars.save(fp)
```
- To load the server variables
```python
# Pass a file path as fp
serverVars.load(fp)
```

### Global User Variables:
- Import package, and create discord_variables_plugin.GlobalUserVariables object:
```python
import discord_variables_plugin
userVars = discord_variables_plugin.GlobalUserVariables()
```
- To set a global user variable
```python
# Pass a discord.User object for user
# Pass a string for varName
# Pass any object for value
userVars.set(user, varName, value)
```
- To get a global user variable
```python
# Pass a discord.User object for user
# Pass a string for varName
# Returns the object stored in varName of user
varNameValue = userVars.get(user, varName)
```
- To clear a saved user
```python
# Pass a discord.User object for user
userVars.clearUser(user)
```
- To remove a variable of a user
```python
# Pass a discord.User object for user
# Pass a string for varName
userVars.removeVar(user, varName)
```
- To save the global user variables
```python
# Pass a file path as fp
userVars.save(fp)
```
- To load the global user variables
```python
# Pass a file path as fp
userVars.load(fp)
```