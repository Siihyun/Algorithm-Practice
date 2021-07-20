function solution(n) {
  let answer = ""
  while(n>0){
      let rest = parseInt(n % 3);
      n = parseInt(n/3);
      
      if(rest === 0 && n !== 0){
        answer = "4" + answer;
        n--;
      }
      else{
        answer = rest + answer;
      }
  }
  

  return answer;
}