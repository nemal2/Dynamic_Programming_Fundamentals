class Item:
    # constructor
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        

def fractional_knapsack(weight, arr):

    arr.sort(key=lambda x: x.profit/x.weight, reverse=True)
    cur_weight = 0
    final_profit = 0.0
    for item in arr:
        if cur_weight + item.weight <= weight:
            cur_weight += item.weight
            final_profit += item.profit
        else:
            diff = weight - cur_weight
            cur_weight += diff
            final_profit += item.profit * (diff / item.weight)
    return final_profit

if __name__ == '__main__':
    
    weight = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    print(fractional_knapsack(weight, arr))
