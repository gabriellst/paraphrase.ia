async function getCurrentTab() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  return tab;
}

const getParaphraseFromServer = async (paraphrase) => {
  const api_url = "http://35.247.218.88/";
  const placeholder = document.getElementById("placeholder_text");
  const results_div = document.getElementById("results");

  placeholder.textContent = "Wait a second, i'm paraphrasing...";
  results_div.setAttribute("loading", "True");
  const data = await fetch(api_url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: paraphrase }),
  })
    .then((response) => response.json())
    .catch(() => {
      results_div.setAttribute("loading", "False");
      placeholder.textContent =
        "Select any text in your browser and click down below!";
      return false;
    });

  results_div.setAttribute("loading", "False");
  placeholder.textContent = "Done! Here are your paraphrases.";
  return data;
};

const createParaphraseList = async (paraphrase) => {
  const results_div = document.getElementById("results");
  const results_list = document.getElementById("results_list");
  const placeholder = document.getElementById("placeholder_text");
  const data = await getParaphraseFromServer(paraphrase);
  const paraphrases = data["data"];
  if (paraphrases) {
    results_list.innerHTML = paraphrases
      .map((item) => `<li>${item}</li>`)
      .join("");
    results_div.setAttribute("hasResult", "True");
    addInstanceListeners();
  } else {
    results_list.innerHTML =
      "<li>There was an error with your request, try again!</li>";
    placeholder.textContent = "Oops! We got a problem...";
    setTimeout(() => {
      placeholder.textContent =
        "Select any text in your browser and click down below!";
    }, 4000);
    results_div.setAttribute("hasResult", "False");
  }
};

const getSelectionFromContentScript = async () => {
  const currentTab = await getCurrentTab();
  const selectionPhrase = await chrome.tabs.sendMessage(currentTab.id, {
    message: "selection",
  });
  return selectionPhrase;
};

const createParaphraseFromSelection = async () => {
  const selectedPhrase = await getSelectionFromContentScript();
  await createParaphraseList(selectedPhrase);
};

const changeSelectedText = async (e) => {
  const paraphrase = e.target.textContent;
  const currentTab = await getCurrentTab();
  chrome.tabs.sendMessage(currentTab.id, {
    message: "changeSelection",
    newParaphrase: paraphrase,
  });
};

const showDetailedListInstance = (e) => {
  if (e.target.classList["copied"]) return;
  const placeholder = document.getElementById("placeholder_text");
  placeholder.textContent = e.target.textContent;
};

const addInstanceListeners = () => {
  const resultsListInstances = document.querySelectorAll(".results li");
  if (resultsListInstances) {
    resultsListInstances.forEach((item) => {
      // item.addEventListener("mouseover", showDetailedListInstance);
      item.addEventListener("click", copyToClipboard);
    });
  }
};

const copyToClipboard = (e) => {
  const text = e.target.textContent;
  navigator.clipboard.writeText(text);
  e.target.classList.toggle("copied");
  e.target.removeEventListener("click", copyToClipboard);
  setTimeout(() => {
    e.target.classList.toggle("copied");
    e.target.addEventListener("click", copyToClipboard);
  }, 2000);
};

const mainButton = document.getElementById("main_button");
mainButton.addEventListener("click", createParaphraseFromSelection);
