
import os
import os.path
import json
import requests

URL= 'http://localhost:5000'
json_path_list = []

def post_lab_spec(file_path):

    with open(file_path) as json_file:
        data = json.load(json_file)
        if 'lab' in data.keys():
            data['lab']['integration_level'] = int(data['lab']['integration_level'])
            end_point = "/labs"
        if 'experiment' in data.keys():
            data['experiment']['integration_level'] = int(data['experiment']['integration_level'])
            end_point = "/experiments"

        data['key'] = 'defaultkey'
        APP_URL = URL + end_point
        headers = {'Content-Type': 'application/json'}
        try:
            response = requests.post(APP_URL, data = json.dumps(data),
                                     headers=headers)
            if response.status_code == 200:
                print "Added json data : " + file_path
            else:
                print "Errore in adding json file " + file_path + " due to " + response.text
        except Exception as e:
            print str(e)
try:
    for dirpath, dirnames, filenames in os.walk(os.getcwd()):
        for filename in [f for f in filenames if f.endswith(".json")]:
            json_path_list.append(os.path.join(dirpath, filename))
except Exception as e:
    print str(e)

for file_path in json_path_list:
    post_lab_spec(file_path)
