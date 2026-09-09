import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    # Map sum -> list of (L, R)
    sum_map = defaultdict(list)
    
    for l in range(1, n + 1):
        curr = 0
        for r in range(l, n + 1):
            curr += a[r - 1]
            sum_map[curr].append((l, r))
            
    bit = [0] * (n + 2)
    
    def add(idx, val):
        while idx <= n:
            bit[idx] += val
            idx += idx & -idx
            
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    total_pairs = 0
    for intervals in sum_map.values():
        if len(intervals) < 2:
            continue
            
        for l, r in intervals:
            total_pairs += query(l - 1)
            add(r, 1)
            
        for l, r in intervals:
            add(r, -1)
            
    print(total_pairs)

if __name__ == "__main__":
    solve()