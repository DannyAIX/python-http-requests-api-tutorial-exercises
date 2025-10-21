import requests

# Your code here

response = requests.get('https://assets.breatheco.de/apis/fake/sample/project1.php')

response_json = response.json()

project_name = response_json['name']
print(project_name)