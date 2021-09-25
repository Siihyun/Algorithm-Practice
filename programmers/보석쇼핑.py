def solution(gems):
    answer = []
    gems_set = set()

    for item in gems:
      gems_set.add(item)
    
    gems_length = len(gems_set)
    s,e = 0,0
    temp_set = set()
    temp_set.add(gems[0])
    length = len(gems)
    min_length = 999999
    while s < length and e < length:
      #print(s+1,e+1,temp_set,min_length)
      if e-s >= min_length:
        if gems[s] not in gems[s+1:e+1]:
          temp_set.discard(gems[s])
        s+=1
        if e < s: e+=1
        continue
      if len(temp_set) == gems_length:
        answer.append([s+1,e+1]) #return [s+1,e+1]
        min_length = min(min_length,e-s)
        if gems[s] not in gems[s+1:e+1]:
          temp_set.remove(gems[s])
        s+=1
        
      else:
        if e!=0 and gems[s] == gems[e]:
          while gems[s] in gems[s+1:e+1]:
            s+=1
        e+=1
        if e < length:
          temp_set.add(gems[e])

    #answer = sorted(answer, key = lambda x : (x[1]-x[0], x[0]))
    for item in answer:
      if item[1]-item[0] == min_length:
        return item
    

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["a","b","a","c","a",'d','e','b','c']))

