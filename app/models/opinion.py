import requests
from bs4 import BeautifulSoup
from app.utils import get_item
import json
import os
from app.parameters import selectors
import pandas as pd

class Opinion:
    def __init__(self, author="", recommendation=None, stars=0,
    content="", useful=0, useless=0, publish_date=None, purchase_date=None, pros=[], cons=[],
    opinion_id=""):
        self.author = author
        self.recommendation = recommendation
        self.stars = stars
        self.content = content
        self.useful = useful
        self.useless = useless
        self.publish_date = publish_date
        self.purchase_date = purchase_date
        self.pros = pros
        self.cons = cons
        self.opinion_id = opinion_id

        return self

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def to_dict(self):
        pass

    def extract_product(self):
        url = "https://www.ceneo.pl/"+id+"#tab=reviews"
        response = requests.get(url)
        page = BeautifulSoup(response.txt, 'html.parser')


        all_opinions = []
        while(url):
            response = requests.get(url)

            page = BeautifulSoup(response.text, 'html.parser')
            self.product_name = get_item(page)



            opinions = page.select("div.js_product-review")
            for opinion in opinions:

                single_opinion = {
                    key:get_item(opinion, *value)
                    for key, value in selectors.items()
                }
                single_opinion["opinion_id"] = opinion["data-entry-id"]
                all_opinions.append(single_opinion)
        
    
            try:
                url = "https://www.ceneo.pl"+get_item(page, "a.pagination__next", "href")
            except TypeError:
                url = None
        
        return self

    def process_stats(self):
        opinions = pd.read__json(json.dumps(self.opinions))

        self.opinions_count = len(self.opinions.index)
        self.pros_count = self.opinions.pros.map(bool).sum()
        self.cons_count = self.opinions.cons.map(bool).sum()
        self.average_score = self.opinions.stars.mean().round(2)
        return self

    def save_opinions(self):
        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")
            
        with open(f"opinions/{self.product_id+}.json", "w", encoding="UTF-8") as jf:
            json.dump(self.opinions, jf, indent=4, ensure_ascii=False)
        return self        

    def extract_opinion(self,opinion):
        for key, value in selectors.items():
            setattr(self, key, get_item(opinion, *value))
        self.opinion_id = opinion
        ["data-entry-id"]
        return self

    

