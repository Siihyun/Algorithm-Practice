function solution(food) {
  var answer = "";
  const [water, ...restFood] = food;
  restFood.forEach((f, idx) => {
    let quantity = Math.floor(f / 2);
    answer += String(idx + 1).repeat(quantity);
  });
  return answer + "0" + answer.split("").reverse().join("");
}
