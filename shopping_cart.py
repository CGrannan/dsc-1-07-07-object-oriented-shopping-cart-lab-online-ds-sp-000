class ShoppingCart:
    # write your code here
    
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
    
    def add_item(self, name, price, quantity=1):
        for i in list(range(quantity)):
            self.total += price 
            self.items.append({'name' : name, 'price' : price})
        return self.total
    
    def mean_item_price(self):        
        return (self.total)/len(self.items)

    def median_item_price(self):
        prices = [i['price'] for i in self.items]
        if len(prices)%2 == 0:
            ind1 = int(len(prices)/2)
            ind2 = ind1-1
            return (prices[ind1] + prices[ind2])/2
        return prices[int(len(prices)/2)]

    def apply_discount(self):
        if self.employee_discount:
            return (self.total*(100 -self.employee_discount))/100
        else:
            return "Sorry, there is no discount to apply to your cart :("

    def void_last_item(self):
        if len(self.items) > 0:
            removed_item = self.items.pop()
            self.total -= removed_item['price']
            return self.total
        else:
            return "There are no items in your cart!"