import requests

# Your code here

projects = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')

projects_json = projects.json()

second_project = projects_json[1]['name']

print(second_project)