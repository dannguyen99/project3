document.querySelectorAll('.btn.btn-white.btn-outline-white').forEach(button => {
  button.onclick = () => {
    if (button.getAttribute('category') === "RL" || button.getAttribute('category') === "SC") {
      const name = button.getAttribute('name');
      console.log(name);
      const type = "pizza";
      const category = button.getAttribute('category');
      $.ajax({
        url: '/order',
        data: {
          'name': name,
          'type': type,
          'category': category
        },
        dataType: 'json',
        success: function(data) {
          alert('Succesfully added to cart' + data.message);
        },
        failure: function(data) {
          alert(data.message);
        }
      });
    }
  }
});
