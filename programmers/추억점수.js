function solution(name, yearning, photo) {
  const answer = [];
  const yearningScore = {};
  for (let i = 0; i < name.length; i++) {
    yearningScore[name[i]] = yearning[i];
  }

  return photo.map((names) =>
    names.reduce((acc, cur) => {
      return acc + (yearningScore[cur] ?? 0);
    }, 0)
  );
}

console.log(
  solution(
    ["may", "kein", "kain", "radi"],
    [5, 10, 1, 3],
    [["may"], ["kein", "deny", "may"], ["kon", "coni"]]
  )
); // [5,15,0]
