from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque([(i, priorities[i]) for i in range(len(priorities))])
    
    while q:
        temp = q.popleft()
        if q and temp[1] < max(q, key = lambda x: x[1])[1]:
            q.append(temp)
        else:
            answer += 1
            if temp[0] == location:
                break
            
    return answer

print(solution([1,1,9,1,1,1], 0))