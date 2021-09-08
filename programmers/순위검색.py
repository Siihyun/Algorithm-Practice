count = 0
t = [['java','c++','python'],['backend','frontend'],['junior','senior'],['pizza','chiken']]
def get_value(idx,tree,query_list):
    key = query_list[idx]
    global count
    if idx == 4:
        if key == '-': key = -1
        for score in tree:
            #print(score,key)
            if int(score) >= int(key):
                count+=1
        return

    if key != '-' and tree.get(key,-1) == -1 : return

    if key == '-':
        for v in tree.values():
            get_value(idx+1,v,query_list)
    
    else:
        get_value(idx+1,tree[key],query_list)



def solution(info, query):
    answer = []
    tree = dict()
    for informations in info:
        information = informations.split()
        cur = tree
        for i in range(3):
            item = information[i]
            if item not in cur.keys():
                cur[item] = dict()
            cur = cur[item]

        #cur[information[4]] = cur.get(information[4],0) + 1
        if cur.get(information[3],0) == 0:
            cur[information[3]] = []
        cur[information[3]].append(information[4])
    
    for q in query:
        global count
        question_list = []
        count = 0
        temp_query = q.split()
        score = temp_query[len(temp_query)-1]
        query_list = temp_query[::2]
        query_list.append(score)
        get_value(0,tree,query_list)
        answer.append(count)
        
    #print(tree['java']['backend']['junior']['pizza'])
    return answer








info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))