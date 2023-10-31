function solution(players, callings) {
  const map = {};

  players.forEach((player, idx) => {
    map[player] = idx;
  });

  callings.forEach((callerName) => {
    const currentRank = map[callerName];
    const 역전주자 = players[currentRank];
    const 뒤쳐진주자 = players[currentRank - 1];
    map[역전주자] -= 1;
    map[뒤쳐진주자] += 1;
    players[currentRank] = players[currentRank - 1];
    players[currentRank - 1] = callerName;
  });

  return players;
}

console.log(
  solution(
    ["mumu", "soe", "poe", "kai", "mine"],
    ["kai", "kai", "mine", "mine"]
  )
); // ["mumu", "kai", "mine", "soe", "poe"]
