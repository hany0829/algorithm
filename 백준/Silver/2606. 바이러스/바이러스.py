n = int(input())
m = int(input())
graph =[[] for i in range(n+1)]
visited = [0] * (n+1)
total = 0

for _ in range(m):
    v1,v2 = map(int,input().split())
    graph[v1].append(v2)  
    graph[v2].append(v1)

def dfs(start):
    stack = [start]
    visited[start]=1

    while stack:
        cur = stack.pop()

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj]=1
                stack.append(adj)
dfs(1)
print(sum(visited)-1)