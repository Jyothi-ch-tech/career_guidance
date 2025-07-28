document.getElementById("quizForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const answers = [
    document.querySelector("input[name='q1']:checked")?.value,
    document.querySelector("input[name='q2']:checked")?.value,
    document.querySelector("input[name='q3']:checked")?.value,
  ];

  const frequency = {};
  answers.forEach(ans => {
    if (ans) {
      frequency[ans] = (frequency[ans] || 0) + 1;
    }
  });

  let recommended = Object.keys(frequency).reduce((a, b) => frequency[a] > frequency[b] ? a : b);

  const branchNames = {
    cse: "Computer Science Engineering (CSE)",
    it: "Information Technology (IT)",
    ece: "Electronics & Communication (ECE)",
    mech: "Mechanical Engineering",
    civil: "Civil Engineering",
    chemical: "Chemical Engineering",
    biotech: "Biotechnology",
    aids: "AI & Data Science"
  };

  document.getElementById("result").textContent = 
    `🔍 Based on your answers, you may enjoy: ${branchNames[recommended] || "a general engineering path"}.`;
});
