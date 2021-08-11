# Discord Variables Plugin
## A plugin to help with saving variables for bots
## Instalation:
- Windows: `pip install discord_variables_plugins`
- Linux: `pip3 install discord_variables_plugins`
## Documentation:
### Server Specific Variables:
- Import package, and create ServerVariables object:
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
# Returns -1 if varName isn't a variable on the server
varNameValue = serverVars.get(guild, varName)
```
- To delete a saved server
```python
# Pass a discord.Guild object for guild
# Returns -1 if the server doesn't exist in the ServerVariables object
serverVars.removeServer(guild)
```
- To remove a variable of a server
```python
# Pass a discord.Guild object for guild
# Pass a string for varName
# Returns -1 if varName isn't a variable on the server
serverVars.removeVar(guild, varName)
```
- To save the server variables
```python
# Pass a file path as fp
# Returns -1 if there was an error saving
serverVars.save(fp)
```
- To load the server variables
```python
# Pass a file path as fp
# Returns -1 if there was an error loading
serverVars.load(fp)
```
