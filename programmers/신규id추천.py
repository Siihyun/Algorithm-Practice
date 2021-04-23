import re

def solution(new_id):
  #1. to lowercase
  new_id = new_id.lower()
  

  #2. to include only a to z, -_.
  new_id = re.sub('[^-_.a-z0-9]','',new_id)
  

  #3. '..' to '.'
  while '..' in new_id:
    new_id = new_id.replace("..",".")
  
  #4.
  if new_id and new_id[0] == '.':
    new_id = new_id[1:]
  
  if new_id and new_id[-1] == '.':
    new_id = new_id[:len(new_id)-1]
  

  #5.
  new_id = new_id if len(new_id) != 0 else 'a'  

  #6.
  if len(new_id) >= 16:
    new_id = new_id[:15]
      
    if new_id[-1] == '.':
      new_id = new_id[:14]
  

  #7.
  while len(new_id) < 3:
    new_id += new_id[-1]
  
  return new_id


id = "...!@BaT#*..y.abcdefghijklm"
print(solution(id))