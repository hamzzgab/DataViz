// vulnerable/js_vuln.js
// INTENTIONAL: demonstrates insecure innerHTML assignment for CodeQL testing only.
function renderUserContent(userInput) {
  const container = document.createElement('div');
  // insecure: injecting raw user input into innerHTML can lead to XSS
  container.innerHTML = userInput;
  document.body.appendChild(container);
}

// Example usage (not executed in CI):
// renderUserContent('<img src=x onerror=alert(1)>');
module.exports = { renderUserContent };
