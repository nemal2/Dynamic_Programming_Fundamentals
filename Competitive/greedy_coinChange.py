def Coin_change(coins,amount):
    coins.sort()
    change = amount
    lis = []
    index = -1

    while True:
        coin = coins[index]
        
        if change == 0:
            break
        elif change >= coin:
            change -= coin
            lis.append(coin)
        else:
            index -= 1
    print(lis)
    print(len(lis))

if __name__ == '__main__':    
    coins = [1,2,5]
    amount = 11
    Coin_change(coins,amount)
