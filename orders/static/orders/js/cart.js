document.querySelectorAll('.btn.btn-white.btn-outline-white').forEach(button => {
  button.onclick = () => {
    const request = new XMLHttpRequest();
    if (button.getAttribute('category') === "RL" || button.getAttribute('category') === "SC") {
      alert(true);
      const name = button.getAttribute('name');
      const type = "pizza";
      const category = button.getAttribute('category');
    } else {
      alert("false");
    }
    request.open('POST', '/order');
    // Callback function for when request completes
    request.onload = () => {
      const data = JSON.parse(request.responseText);

      // Update the result div
      if (data.success) {
        alert("Success");
      } else {
        alert(data.message)
      }
    }
    const data = new FormData();
    data.append('name', name);
    data.append('type', type);
    data.append('category', category);
    // Send request
    request.send(data);
    return false;
  }
})
