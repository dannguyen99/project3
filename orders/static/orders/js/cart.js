document.querySelectorAll('.btn.btn-white.btn-outline-white').forEach(button => {
  button.onclick = () =>{
    if( button.getAttribute('category')){
      alert("true");
    }
    else{
      alert("false");
    }
  }
})
