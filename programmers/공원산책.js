function solution(park, routes) {
  const d = {
    E: [0, 1],
    W: [0, -1],
    N: [-1, 0],
    S: [1, 0],
  };
  const map = park.map((p) => p.split(""));
  const currentPos = {};

  currentPos.x = park.findIndex((p) => p.includes("S"));
  currentPos.y = park[currentPos.x].indexOf("S");

  const LIMIT_X = map.length;
  const LIMIT_Y = map[0].length;

  routes.forEach((route) => {
    let [direction, moveCount] = route.split(" ");
    const saveX = currentPos.x;
    const saveY = currentPos.y;
    let success = true;
    while (moveCount--) {
      let { x, y } = currentPos;
      const [nextX, nextY] = [x + d[direction][0], y + d[direction][1]];

      if (
        nextX < 0 ||
        nextX >= LIMIT_X ||
        nextY < 0 ||
        nextY >= LIMIT_Y ||
        map[nextX][nextY] === "X"
      ) {
        success = false;
        break;
      }
      currentPos.x += d[direction][0];
      currentPos.y += d[direction][1];
    }
    if (!success) {
      currentPos.x = saveX;
      currentPos.y = saveY;
    }
  });

  return [currentPos.x, currentPos.y];
}

console.log(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"])); // [2,1]
