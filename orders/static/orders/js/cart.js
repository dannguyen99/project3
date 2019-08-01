document.querySelectorAll('select').forEach(option => {
  option.onchange = () => {
    option.parentElement.parentElement.parentElement.querySelector('.price').innerHTML = option.value;
  }
})

document.querySelectorAll('.btn.btn-white.btn-outline-white').forEach(button => {
  button.onclick = () => {
    if (button.getAttribute('category') === "RL" || button.getAttribute('category') === "SC") {
      const name = button.getAttribute('name');
      const type = "pizza";
      const category = button.getAttribute('category');
      $.ajax({
        url: '/remove',
        data: {
          'name': name,
          'type': type,
          'category': category
        },
        dataType: 'json',
        success: function(data) {
          alert('Succesfully removed from cart');
          button.parentElement.parentElement.parentElement.style.display = 'none';
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
        url: '/remove',
        data: {
          'name': name,
          'type': type
        },
        dataType: 'json',
        success: function(data) {
          alert("Succesfully removed from cart");
          button.parentElement.parentElement.parentElement.style.display = 'none';
        },
        failure: function(data) {
          alert(data.message);
        }
      });
    }
  }
});
document.querySelector('#confirm').onclick = () =>{
  $.ajax({
    url: '/confirm',
    success: function(data) {
      alert("You food is comming");
      window.location.href = "http://127.0.0.1:8000/menu";
    },
    failure: function(data) {
      alert(data.message);
    }
  })
}
