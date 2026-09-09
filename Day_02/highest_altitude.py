import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    gain = [int(x) for x in input_data[1:n+1]]
    
    current_altitude = 0
    max_altitude = 0
    
    for g in gain:
        current_altitude += g
        if current_altitude > max_altitude:
            max_altitude = current_altitude
            
    print(max_altitude)

if __name__ == '__main__':
    solve()