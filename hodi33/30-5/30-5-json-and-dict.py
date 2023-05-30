import json

d1 = {'name': 'saar',
      'salary': 90000,
      'address': {
          'city': 'lod',
          'street': 'hagiiboor 5',
          'zip code': 195000
      },
      'single': True}
json_statham = '{"name": "json statham", "salary": 900000, "address": {"city": "holly wood", "street": "laviva", "zip code": 98991}, "single": false}'

# print(type(d1))
# j1 = json.dumps(d1)  # convert a dict to json look alike str
# print(type(j1))
# print(j1)
json_statham_d1=json.loads(json_statham) # convert a str to dict
print(type(json_statham_d1))