from collections import defaultdict

graph = defaultdict(list)

v,e = map(int , input().split())

for i in range(e):
    u,v = map(str, input().split())
    graph[u].append(v)
    graph[v].append(u)

for v in graph:
    print(v,graph[v])