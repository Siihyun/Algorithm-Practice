function solution(str, m) {
  let startIndex = 0;
  let lastIndex = 0;
  let mapObj = {};
  let answer = 0;

  while (lastIndex < str.length) {
    // 현재 상태로 lastIndex를 뒤로 보낼 수 있는지 체크
    const currentNumberOfChar = Object.values(mapObj).filter(
      (v) => v > 0
    ).length;

    // 문자열 제한 개수를 초과한 경우, startIndex를 하나 뒤로 밀어줍니다.
    if (currentNumberOfChar > m) {
      const charTobeDeleted = str[startIndex];
      mapObj[charTobeDeleted] -= 1;
      startIndex += 1;
      continue;
    }

    const currentChar = str[lastIndex];

    let success = true;
    if (!mapObj[currentChar]) {
      mapObj[currentChar] = 1;
      if (currentNumberOfChar === m) success = false;
    } else {
      mapObj[currentChar] += 1;
    }
    lastIndex++;

    const adjust = success ? 0 : -1;
    answer = Math.max(
      answer,
      Object.values(mapObj).reduce((acc, cur) => acc + cur, 0) + adjust
    );
  }
  return answer;
}

console.log(solution("ababcbcbaaabbdef", 2)); // 6
console.log(solution("aaaaaaa", 2)); // 7
console.log(solution("", 2)); // 0
console.log(solution("abababcdcdcdcdcd", 2)); // 10
console.log(solution("abcdefghijklmnop", 1)); // 1
console.log(solution("abcdefghijklmnopqrstuvwxyz", 1000)); // 26
