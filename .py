class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        ret = [None]*n
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
        isCycle = False
        def dfs(u,path):
            nonlocal isCycle
            path[u] = True
            res = defaultdict(int)
            for v in adj[u]:
                if(path[v]):
                    isCycle = True
                if(not isCycle and not ret[v]): dfs(v,path)
                if(isCycle): return
                for c in ret[v]:
                    res[c] = max(res[c],ret[v][c])
            res[colors[u]]+=1
            ret[u] = res
            path[u] = False

        vis = [False]*n
        res = 0
        for u in range(n):
            if not ret[u]: dfs(u,vis)
            if(isCycle): return -1
            res = max(res,max(ret[u].values()))
        return res
