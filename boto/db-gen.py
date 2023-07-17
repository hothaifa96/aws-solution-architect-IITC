import boto3
from flask import *

db = boto3.client('dynamodb')


def send_item(username, height, kwargs):
    item_to_add = {
        "username": {"S": username},
        "height": {"N": height},
        kwargs[0]: {kwargs[1]: kwargs[2]}
    }
    # add item to table
    res = db.put_item(TableName='Users', Item=item_to_add)


def get_items():
    # res = db.get_item() # search using pk
    res = db.scan(TableName='Users')
    data = res['Items']

    for d in data:
        print(d['username']['S'])
    return data


app = Flask(__name__)


@app.get('/users')
def get_all_users():
    data = get_items()
    return data, 200

@app.post('/users')
def add_users():
    print(request.get_json())
    item = request.get_json()
    send_item(item['username'],item['height'],item['kwargs'])
    return 'OK', 201


app.run()