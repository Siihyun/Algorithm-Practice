function solution(n) {
  let answer = ""
  while(n){
      let rest = parseInt(n % 3);
      n = n/3;
      if(rest === 0){
        answer += "4";
        n--;
      }
      else{
        answer += rest;
      }
  }
  return answer;
}