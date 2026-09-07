import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    col = ord(s[0]) - ord('a') + 1
    row = int(s[1])
    
    if (col + row) % 2 == 0:
        print("Black")
    else:
        print("White")

if __name__ == "__main__":
    solve()
