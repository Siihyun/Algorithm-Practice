function solution(s) {
  return (
    s
      .toLowerCase()
      .split("")
      .reduce((a, c) => (c === "p" ? a + 1 : a), 0) ===
    s
      .toLowerCase()
      .split("")
      .reduce((a, c) => (c === "y" ? a + 1 : a), 0)
  );
}

function solution2(s) {
  return (
    s.toLowerCase().split("p").length === s.toLowerCase().split("y").length
  );
}

console.log(solution("pPoooyY")); // true
