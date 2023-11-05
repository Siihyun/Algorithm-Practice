function solution(n, m, section) {
  let answer = 0;
  const standard = m - 1;
  let cover = 0;

  section.forEach((v) => {
    if (cover < v) {
      answer++;
      cover = v + standard;
    }
  });
  return answer;
}
