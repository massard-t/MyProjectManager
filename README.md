# MyProjectManager
Python-based tool to assist IT students in their projects

## Optimize My Time
Task optimisation based on Gantt's diagramms, opening in a temporary web browser.<br>
TaskName;TSK;\[ABV\](Abbreviation for the needed tasks)

## Create My Base
Asks the user for informations about the project (language, templates, etc...)<br>

## I Am Working
Record the time, i.e. "MPM --IAW (start|stop)" in a JSON file.<br>
You can specify the task you're working on. "MPM --IWAS (start|stop) --task ABV"

## Did The Task
Record the said task as done. "MPM --DTD ABV"<br>

## Watch Those Files
Check the coding format, using a custom coding style (PyV8, Pyflake...)<br>
"MPM --WTF (PF, P8, ET)"

## Run Collab Mod
Start a REST based server, to work with other people. They'll be able to modify the state of the different tasks.<br>
"MPM --RCM [port]"

## Kill My Day
Saves, records changes if asked to, commits on (SVN|GIT) if asked to.<br>
"MPM --KMD KTHBYE"


