import json
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

print('APP ROOT_PATH =', app.root_path)
try:
    print('TEMPLATES DIR LISTING =', os.listdir(os.path.join(app.root_path, 'templates')))
except Exception as e:
    print('TEMPLATES LISTING ERROR:', e)

with open('projects.json', 'r') as f:
    projects = json.load(f)

@app.route("/")
def main():
    filtered_projects = [
        {
            'id': p['id'],
            'projectname': p['projectname'],
            'projectyear': p['projectyear']
        }
        for p in projects
    ]
    return render_template('index.html', projects=filtered_projects)

@app.route("/project/<int:id>")
def project(id):
    project_data = next((p for p in projects if p['id'] == id), None)
    return render_template('project.html', project=project_data)