const getSelectionElement = () => {
  return window.getSelection();
};

getSelectionString = () => {
  return window.getSelection().toString();
};

chrome.runtime.onMessage.addListener((request, sender, response) => {
  const text = getSelectionString();
  if (text) {
    response(text);
    return true;
  }
});
