times = [0] * 360000

def cal(t):
  time, min, sec = map(int,t.split(':'))
  t_sec = time*3600 + min*60 + sec
  
  return t_sec
  


def solution(play_time, adv_time, logs):
  
    
  for log in logs:
    start,end = log.split('-')
    start_sec = cal(start)
    end_sec = cal(end)
    for i in range(start_sec,end_sec+1):
      times[i]+=1
    
  time_length = cal(play_time) - cal(adv_time)
  adv = cal(adv_time)
  #print(time_length)
  
  cur_sum = sum(times[0:adv+1])
  max_value = cur_sum 
  max_idx = 0
  for i in range(1,time_length):
    #cur_sum -= sum(times[i:i+adv+1])
    cur_sum -= times[i-1]
    cur_sum += times[i+adv]
    #init_sum = sum(tims[0:adv+1])
    if max_value < cur_sum :
      max_idx = i
      max_value = cur_sum
  
  #print(max_idx)
  sec = str(max_idx%60)
  max_idx = max_idx//60
  min = str(max_idx%60)
  max_idx = max_idx//60
  hour = str(max_idx)

  if len(sec) == 1: sec = '0' + sec
  if len(min) == 1: min = '0' + min
  if len(hour) == 1: hour = '0' + hour
  return hour + ':' + min + ':' + sec

print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))