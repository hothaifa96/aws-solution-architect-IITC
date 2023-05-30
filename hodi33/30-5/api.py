import requests

# url = r'https://jsonplaceholder.typicode.com/users'
# res = requests.get(url)
# if 200 <= res.status_code <400:
#     print(f'{res.status_code} this is the code ')
#     users = res.json()
#     for user in users:
#         for k,v in user.items():
#             print(f'{k} -> {v}')
#         print('-'*100)
# else:
#     print(f'naaaaaah {res.status_code}')
#
# # print the body of all the comments with postId of 2 from this url
# url = https://jsonplaceholder.typicode.com/comments

res = requests.get('https://jsonplaceholder.typicode.com/comments')

comments = res.json()
for comment in comments:
    if comment['postId'] in [2, 3, 5]:  # post id 2 or 3 or 5
        print(comment['body'])
        print('*' * 100)
