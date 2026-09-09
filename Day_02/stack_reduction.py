import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    stack = []
    
    for x in a:
        if x >= 0:
            stack.append(x)
        else:
            target = abs(x)
            current_removed_sum = 0
            
            while stack and current_removed_sum < target:
                current_removed_sum += stack.pop()
                
            stack.append(target)
            
    print(sum(stack))

if __name__ == '__main__':
    solve()