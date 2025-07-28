const branches = [
  {
    name: "CSE (Core)",
    image: "assets/images/cse.jpg",
    info: "Focuses on programming, algorithms, OS, DBMS, and placements in product-based companies."
  },
  {
    name: "IT",
    image: "assets/images/it.jpg",
    info: "Covers networking, software engineering, system admin, and is close to CSE in scope."
  },
  {
    name: "AIML",
    image: "assets/images/aiml.jpg",
    info: "Specializes in AI/ML topics, Python, Deep Learning. Good for data science careers."
  },
  {
    name: "AIDS",
    image: "assets/images/aids.jpg",
    info: "Focus on data handling, analysis, statistics. Ideal for data analyst/data scientist roles."
  },
  {
    name: "CIC",
    image: "assets/images/cic.jpg",
    info: "Cybersecurity, networks, cloud computing, and secure systems. Focused career path."
  }
];

const container = document.getElementById("cardContainer");

branches.forEach(branch => {
  const card = document.createElement("div");
  card.className = "card";

  card.innerHTML = `
    <img src="${branch.image}" alt="${branch.name}">
    <h3>${branch.name}</h3>
    <p>${branch.info}</p>
  `;

  container.appendChild(card);
});
