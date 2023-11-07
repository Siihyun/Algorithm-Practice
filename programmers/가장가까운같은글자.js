function solution(s) {
  const answer = [];
  const mapIndex = {};
  s.split("").forEach((t, idx) => {
    mapIndex[t] !== undefined
      ? answer.push(idx - mapIndex[t])
      : answer.push(-1);
    mapIndex[t] = idx;
  });
  return answer;
}
