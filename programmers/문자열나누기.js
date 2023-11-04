function solution(s) {
  let answer = 0;
  let x = 0;
  let exceptX = 0;
  let standardChar = s[0];

  for (let i = 0; i < s.length; i++) {
    const curChar = s[i];
    if (x === 0) {
      x = 1;
      standardChar = s[i];
      continue;
    }
    curChar === standardChar ? x++ : exceptX++;

    if (x === exceptX) {
      answer++;
      x = 0;
      exceptX = 0;
    }
  }
  if (x !== 0 || exceptX !== 0) answer++;
  return answer;
}

console.log(solution("banana")); // 3
console.log(solution("abracadabra")); // 6
console.log(solution("aaabbaccccabba")); // 3
