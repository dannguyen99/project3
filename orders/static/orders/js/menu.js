document.querySelectorAll('.btn.btn-white.btn-outline-white').forEach(button => {
  button.onclick = () => {
    if (button.getAttribute('category') === "RL" || button.getAttribute('category') === "SC") {
      const name = button.getAttribute('name');
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
          alert('Succesfully added to cart');
        },
        failure: function(data) {
          alert(data.message);
        }
      });
    }
    else{
      const name = button.getAttribute('name');
      const type = button.getAttribute('type');
      $.ajax({
        url: '/order',
        data: {
          'name': name,
          'type': type
        },
        dataType: 'json',
        success: function(data) {
          alert("Succesfully added to cart");
        },
        failure: function(data) {
          alert(data.message);
        }
      });
    }
  }
});
