from itertools import combinations
def solution(orders, course):
    answer = []
    
    for num in course:
        hash = {}

        for order in orders:
            combs = list(combinations(sorted(order),num))
            for comb in combs:
                hash[comb] = hash.get(comb,0) + 1
        
        if len(hash) == 0: continue
        hash = sorted(hash.items(), key=lambda x : x[1], reverse = True)

        
        max_val = hash[0][1]
        if max_val < 2 : continue
        answer.append(''.join(map(str,hash[0][0])))
        
        for i in range(1,len(hash)):
            if hash[i][1] != max_val: break
            answer.append(''.join(map(str,hash[i][0])))

        
    return sorted(answer)