import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(T):
        n = int(input_data[idx])
        s = input_data[idx + 1]
        idx += 2
        
        # Split by 'W' to isolate contiguous segments of 'R' and 'B'
        segments = s.split('W')
        possible = True
        
        for seg in segments:
            if not seg:
                continue
            has_r = 'R' in seg
            has_b = 'B' in seg
            if not (has_r and has_b):
                possible = False
                break
                
        out.append("YES" if possible else "NO")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()