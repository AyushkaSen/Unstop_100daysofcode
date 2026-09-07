import sys
from collections import Counter

def solve():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    n = int(lines[0].strip())
    strings = [lines[i].strip() for i in range(1, n + 1)]
    k = int(lines[n + 1].strip())
    
    counts = Counter(strings)
    
    unique_count = 0
    for s in strings:
        if counts[s] == 1:
            unique_count += 1
            if unique_count == k:
                print(s)
                return
                
    print(-1)

if __name__ == "__main__":
    solve()
