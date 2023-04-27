from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = deque([math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))])
    
    cur_days = days.popleft()
    count = 1
    
    while days:
        temp = days.popleft()
        if cur_days >= temp:
            count += 1
        else:
            cur_days = temp
            answer.append(count)
            count = 1
            
    answer.append(count)
    
    return answer