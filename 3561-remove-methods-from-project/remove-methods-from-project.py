class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build an adjacency list for the invocations graph
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Step 2: Use BFS to find all suspicious methods
        suspicious = {k}
        queue = [k]
        
        # Traverse to find all methods invoked by the suspicious method
        for node in queue:
            for neighbor in adj[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Step 3: Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # We can't safely remove the methods, return all methods
                return list(range(n))
                
        # Step 4: Return the remaining non-suspicious methods
        return [i for i in range(n) if i not in suspicious]