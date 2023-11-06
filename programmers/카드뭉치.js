function solution(cards1, cards2, goal) {
  while (goal.length !== 0) {
    const word = goal[0];
    if (cards1[0] !== word && cards2[0] !== word) {
      return "No";
    }
    if (cards1[0] === word) cards1.shift();
    if (cards2[0] === word) cards2.shift();
    goal.shift();
  }
  return goal.length === 0 ? "Yes" : "No";
}

console.log(
  solution(
    ["i", "drink", "water"],
    ["want", "to"],
    ["i", "want", "to", "drink", "water"]
  )
); // "Yes"
