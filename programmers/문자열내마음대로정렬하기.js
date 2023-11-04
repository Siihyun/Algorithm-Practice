function solution(strings, n) {
  const standards = strings.reduce((acc, cur) => {
    return acc + cur[n];
  }, "");

  return strings.sort((a, b) => {
    if (a[n] < b[n]) return -1;
    else if (a[n] > b[n]) return 1;
    else {
      if (a < b) return -1;
      if (a > b) return 1;
      else return 0;
    }
  });
}

console.log(solution(["sun", "bed", "car"], 1)); // ["car", "bed", "sun"]
