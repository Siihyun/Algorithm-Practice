function solution(s) {
  return s
    .split(" ")
    .map((word) => {
      if (word === "") return word;
      const [firstLetter, ...rest] = word.split("");
      return `${firstLetter.toUpperCase()}${rest.join("").toLowerCase()}`;
    })
    .join(" ");
}

console.log(solution("3people unFollowed me")); // "3people Unfollowed Me"
console.log(solution("for the last week")); // "For The Last Week"
