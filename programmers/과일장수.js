function solution(k, m, score) {
  let answer = 0;
  score.sort((a, b) => b - a);
  const t = score.length % m;

  for (let i = 0; i < score.length - t; i = i + m) {
    answer += score[i + m - 1] * m;
  }
  return answer;
}
