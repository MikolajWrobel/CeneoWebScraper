class Product:
    def __init__(self, product_id=0, opinions=[], product_name="", opinions_count=0, pros_count=0, cons_count=0, average_score=0):
        self.product_id = product_id
        self.product_name = product_name
        self.opinions = opinions
        self.opinions_count = opinions_count
        self.pros_count = pros_count
        self.cons_count = cons_count
        self.average_score = average_score

        return self
    
