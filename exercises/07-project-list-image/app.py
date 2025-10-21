import requests

# Your code here

projects = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')


projects_json = projects.json()

last_project = projects_json[-1]

last_image_url = last_project['images'][-1]

print(last_image_url)