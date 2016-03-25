## MyProjectManager
Python-based tool to assist IT students in their projects

# Optimize My Time
Task optimisation based on Gantt's diagramms, opening in a temporary web browser
TaskName;TSK;[ABV](Abbreviation for the needed tasks)

# Create My Base
Asks the user for informations about the project (language, templates, etc...)

# I Am Working
Record the time, i.e. "MPM --IAW (start|stop)" in a JSON file. 
You can specify the task you're working on. "MPM --IWAS (start|stop) --task ABV"

# Did The Task
Record the said task as done. "MPM --DTD ABV"

# Watch Those Files
Check the coding format, using a custom coding style (PyV8, Pyflake...)
"MPM --WTF (PF, P8, ET)"

# Run Collab Mod
Start a REST based server, to work with other people. They'll be able to modify the state of the different tasks.
"MPM --RCM [port]"

# Kill My Day
Saves, records changes if asked to, commits on (SVN|GIT) if asked to.
"MPM --KMD KTHBYE"


