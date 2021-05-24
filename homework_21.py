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


dict1 = {




        "name": "Natalia Oreiro",
        "url_":"http://t2.gstatic.com/licensed-image?q=tbn:ANd9GcT3_8PjjUpfY8hTiGR0xqp44kD16ksLOzJAn0GNjSkxi4S1RWQCuq_wCACvjDvz"
    }
dict2 = {
        "name": "jessica simpson",
        "url_":"https://upload.wikimedia.org/wikipedia/commons/f/f2/Jessica_Simpson_Joining_Forces_with_the_Rockies_April_2011_%28cropped%29.jpg"
    }
dict3 = {
        "name": "Adel",
        "url_":"https://uk.toluna.com//dpolls_images/2016/04/23/5bc72609-421c-4067-b66e-135d028b76b8.jpg"
    }
json_dump = json.dumps(dict1,dict3,dict2)
print(json_dump)
# with open("sample_json.json", 'r') as json_in

    # response = requests.get(json_dump[dict_][name])
    # print(response)
    # with open(name, 'wb') as file:
    #     file.write(response.content)


# print(response.text)
#
# print(response.json())