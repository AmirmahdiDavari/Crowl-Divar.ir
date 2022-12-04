import scrapy

url = "https://divar.ir/v/-/{token}"

token_file = open('/Users/ASUS/Desktop/scrapy/Divar/Divar/tokens.txt', 'r', encoding='utf8')

tokens = token_file.read().split(',')
token_file.close()


class DivarSpider(scrapy.Spider):
    name = 'divar'
    user_agent = {
        'authorization': 'Basic eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NTc1MjUzLCJpYXQiOjE2Njc0MDI0NTMsImp0aSI6IjIwMjJhOTQzMTU1ZTQxNWY5ZTA2YTI2YWI0MmI2MjA5IiwidXNlcl9pZCI6MTB9.0ImpdESJt5vgmYUjXiMWlLOaPUGvYOE_bigbIrdTDHE',
        'Content-Type': 'application/json'}

    start_urls = [url.format(token=token) for token in tokens]

    def parse(self, response, **kwargs):
        Info=response.css('div span.kt-group-row-item__value::text')
        # contact=response.css('div button..post-actions__get-contact').click()

        area=int(Info[0].extract())
        construction=int(Info[1].extract())
        room=int(Info[2].extract())
        asansor=Info[3].extract()
        parking=Info[3].extract()
        storeRoom=Info[3].extract()
        price=response.css('div p.kt-unexpandable-row__value::text')[0].extract()
        print(price)
        print('----------------------------')
        print(area)
        print('----------------------------')
        print(construction)
        print('----------------------------')
        print(room)
        print('----------------------------')
        print(asansor)
        print('----------------------------')
        print(parking)
        print('----------------------------')
        print(storeRoom)
        print('----------------------------')
        yield {
        "area":area,
        "construction":construction,
        "room":room,
        "asansor":asansor,
        "parking":parking,
        "storeRoom":storeRoom,
        "price":price,
        # "contact":contact,
        }


