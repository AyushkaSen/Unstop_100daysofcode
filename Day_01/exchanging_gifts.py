import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        out_degree[u] += 1
        in_degree[v] += 1
        idx += 2
        
    for i in range(1, n + 1):
        if in_degree[i] == n - 1 and out_degree[i] == 0:
            print(i)
            return
            
    print(-1)

if __name__ == "__main__":
    solve()
