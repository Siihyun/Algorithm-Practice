function solution(k, score) {
  const answer = [];
  const honer = [];
  score.forEach((s) => {
    honer.push(s);
    honer.sort((a, b) => a - b);
    if (honer.length > k) honer.shift();
    answer.push(honer[0]);
  });
  return answer;
}
