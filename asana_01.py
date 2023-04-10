# import requests

import json
import os
from datetime import datetime
import asana

# GET Enviroment variables - Configuration settings
## get environment variables for PTV API
pattok = os.environ.get("ASANA_PT_ACCTOK")
guid = os.environ.get("ASANA_GUID")

client = asana.Client.access_token(pattok)
# result = client.workspaces.get_workspace(guid, fields="")

# find the gid of the first project
result = client.projects.get_projects_for_workspace(guid, {'param': 'value', 'param': 'value'})#, opt_pretty=True)
project_gid = [i for i in result][0]['gid']

# list all taks from the porject
tasklist = client.tasks.get_tasks_for_project(project_gid, {'param': 'value', 'param': 'value'}, opt_pretty=True)

[print(i) for i in tasklist]