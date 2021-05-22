import json
import os
import yaml
1 json to txt parser
with open("sample_json.json", "r") as json_file, open('sample_json.txt', 'w') as outfile:
    data = json.load(json_file)
    json.dump(data, outfile)
2  json to yaml parser
with open("sample_json.json", 'r') as json_in, open("sample_json.yml", "w") as yaml_out:
    json_object = json.load(json_in)
    yaml.dump(json_object, yaml_out)
3 Yaml to json parser
with open("sample_yaml.yml", 'r') as yaml_in, open("sample_yaml.json", "w") as json_out:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, json_out)
4 Yaml to text parser
with open("sample_yaml.yml", "r") as yaml_file, open('sample_yaml.txt', 'w') as outfile:
    data = yaml.safe_load(yaml_file)
    yaml.dump(data, outfile)