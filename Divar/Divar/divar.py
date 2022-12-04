import requests

url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'
last_post_date = 1670095098402530
data = {"json_schema": {"category": {"value": "apartment-sell"}, "cities": ["1"]}, "last-post-date": last_post_date}
headers = {"Content-Type": "application/json"}
res = requests.post(url, json=data, headers=headers)
data = res.json()
last_post_date = data['last_post_date']
count = 0
list_of_tokens = []
while True:
    print('---------------------------------------')
    url = 'https://api.divar.ir/v8/web-search/1/apartment-sell'
    data = {"json_schema": {"category": {"value": "apartment-sell"}, "cities": ["1"]},
            "last-post-date": last_post_date}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url, json=data, headers=headers)
    data = res.json()
    last_post_date = data['last_post_date']
    for widget in data['web_widgets']['post_list']:
        token = widget['data']['token']
        print(token)
        list_of_tokens.append(token)

        count += 1
    if count >= 100:
        break
csvFile = open('tokens.txt', 'w', encoding='utf8')
csvFile.write(','.join(list_of_tokens))
csvFile.close()
