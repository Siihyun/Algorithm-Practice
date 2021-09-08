import re

def solution(new_id):
    answer = ''
    
    #1
    new_id = new_id.lower()

    #2
    new_id = re.sub('[^0-9a-z-_.]','',new_id)

    #3
    while '..' in new_id:
        new_id = new_id.replace('..','.');
    
    #4
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:len(new_id)-1]
    
    #5
    if len(new_id) == 0:
        new_id = 'a'
    
    #6
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    
    #7
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1]
    
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))