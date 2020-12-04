import requests
import json
from random import randint
class Drinks:
    def __init__(self,url,post_url,num):
        self.url = url
        self.post_url = post_url
        self.num = num
    def get_drinks(self):
        for i in range(int(self.num)) :
            try:
                request = requests.get(self.url)
                if request.status_code == 200 :
                    1 == 1
                else :
                    raise Exception ('Bad status code - ' + str(request.status_code))
                json_text = json.loads(request.text)            
                drinks = (json_text['drinks'])
                for item in json_text['drinks']:
                    1 == 1
                new_item = {}
                ident = item['idDrink']
                new_item['author'] = item['strDrink']
                new_item['quote'] = item['strInstructions']
                new_json = json.dumps(new_item)
            except :
                raise Exception ('Somethin wrong')  
        return new_item
    def post_api_app(self): 
        for i in range(int(self.num)):
            request_post = requests.post(
                self.post_url + str(randint(100,1000)),
                data=Drinks.get_drinks(self))
            s = json.loads(request_post.text)
start = Drinks(post_url='http://127.0.0.1:5000/ai-quotes/',url='https://www.thecocktaildb.com/api/json/v1/1/random.php',num='10')
start.post_api_app()
