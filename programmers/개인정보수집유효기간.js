function solution(today, terms, privacies) {
  const answer = [];
  const todayDate = new Date(today.split(".").join("-"));
  const termsMap = terms.reduce((before, cur) => {
    const [name, period] = cur.split(" ");
    return { ...before, [name]: Number(period) };
  }, {});

  privacies.forEach((privacy, idx) => {
    const [dateString, name] = privacy.split(" ");
    const termsDate = new Date(dateString.split(".").join("-"));
    termsDate.setMonth(termsDate.getMonth() + termsMap[name]);

    if (todayDate.getTime() >= termsDate.getTime()) answer.push(idx + 1);
  });
  return answer;
}
