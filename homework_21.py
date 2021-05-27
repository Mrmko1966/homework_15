import requests
import json
class Actor(object):
    def __init__(self, name, surname, url):
        self.name = name
        self.surname = surname
        self.url = url

    def to_json(self):
        data_ = {
            'name': self.name,
            'surname': self.surname,
            'age': self.url
        }
        return data_
    def __repr__(self):
        return F"{self.name}-{self.surname} {self.url}"

with open("sample_json.json", "r") as json_file:
    data = json.load(json_file)

for item in data["items"]:
    response = requests.get(item["url"])
    a= "{} {}".format(item["name"],item["surname"])

    with open(F"{a}.jpeg", 'wb') as file:
        file.write(response.content)


