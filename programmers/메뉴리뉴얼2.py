from itertools import combinations

def solution(orders, course):
    answer = []
    candidates = dict()

    for c in course:
        print("course : ",c)
        temp_candidate = dict()
        for order in orders:
            order = sorted(order)
            #print('order : ',order)
            combis = list(combinations(order,c))
            for combi in combis:
                key = ''.join(combi)
                temp_candidate[key] = temp_candidate.get(key,0) + 1
        sorted_dict = sorted(temp_candidate.items(), key = lambda item: item[1], reverse=True)
        
        standard = 0
        print(sorted_dict)
        if len(sorted_dict) != 0 : standard = sorted_dict[0][1]
    
        for item in sorted_dict:
            if item[1] != standard: break
            candidates[item[0]] = item[1]
        print("candidates: ",candidates)

    candidates = sorted(candidates.items())
    #print("candidates outside: ",candidates)
    for candidate in candidates:
        if candidate[1] >= 2:
            answer.append(candidate[0])
    return answer

print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))