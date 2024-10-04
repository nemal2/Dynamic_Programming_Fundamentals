def knaspack_tabular(profit, weight, capacity,n):

    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
            elif weight[i - 1] <= w:
                table[i][w] = max(profit[i - 1] + table[i - 1][w - weight[i - 1]], table[i - 1][w])
            else:
                table[i][w] = table[i - 1][w]
    return table[n][capacity]

if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    n = len(profit)
    print(knaspack_tabular(profit, weight, capacity, n))
