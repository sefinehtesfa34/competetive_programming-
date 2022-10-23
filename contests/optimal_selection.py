from cmath import inf


class Solution:
    def get_num_of_products(self):
        return int(input())
    
    def get_prices(self, num_products):
        prices = []
        for  _ in range(num_products):
            
            prices.append(list(map(int, input().split())))
        return prices 
    
    def optimal_selection(self):
        num_products = self.get_num_of_products()
        prices = self.get_prices(num_products)       
        return print(self.top_down(0, prices, num_products, [0]*(len(prices[0]))))
              
    def top_down(self, index, prices, num_products, chosen):
        if num_products == index:
            return 0
        current_nth_prices = prices[index]
        total = inf
        for product, current_price in enumerate(current_nth_prices):
            if chosen[product - 1] == 0: 
                chosen[product - 1] = 1
                total = min(total, current_price + self.top_down(index + 1, prices, num_products, chosen))
                chosen[product - 1] = 0
        return total 
    
    '''
    dp[]
    6 9 8 8 8 7 8 6 2 4 
    
    '''
solution = Solution()
solution.optimal_selection()
    
        