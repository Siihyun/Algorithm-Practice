function solution(s, skip, index) {
  let alphabets = "abcdefghijklmnopqrstuvwxyz";
  skip.split("").forEach((i) => {
    alphabets = alphabets.replace(i, "");
  });

  return s
    .split("")
    .map((target) => {
      const targetIndex = alphabets.indexOf(target);
      return alphabets[(targetIndex + index) % alphabets.length];
    })
    .join("");
}
