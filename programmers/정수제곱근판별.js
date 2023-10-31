function solution(n) {
  let answer = -1;
  for (let i = 0; i <= Math.sqrt(n); i++) {
    if (Math.pow(i, 2) === n) answer = Math.pow(i + 1, 2);
  }
  return answer;
}

console.log(solution(121)); // 144
console.log(solution(3)); // -1
