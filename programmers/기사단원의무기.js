function solution(number, limit, power) {
  function getYaksu(n) {
    const s = new Set();
    const limit = Math.sqrt(n);

    for (let i = 1; i <= limit; i++) {
      if (n % i === 0) {
        s.add(i);
        s.add(n / i);
      }
    }
    return s.size;
  }

  let answer = 0;
  for (let i = 0; i <= number; i++) {
    const r = getYaksu(i);
    answer += r <= limit ? r : power;
  }
  return answer;
}
