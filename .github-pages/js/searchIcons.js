// HoI4 Mod Icon Search by Yard1 
// Based on code from https://www.w3schools.com/

function searchIcons() {
  var input, filter, div, i, txtValue;
  input = document.getElementById('searchInput');
  filter = input.value.toUpperCase();
  div = document.getElementsByClassName("icon");

  for (i = 0; i < div.length; i++) {
    txtValue = div[i].getAttribute("title");
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      div[i].style.display = "";
    } else {
      div[i].style.display = "none";
    }
  }
}

function toggleIcons(id) {
  var checkBox = document.getElementById(id);
  var elementToHide;
  if (id === 'ideas-toggle') {
    elementToHide = document.getElementById('ideasSection');
  } else {
    elementToHide = document.getElementById('goalsSection');
  }

  if (checkBox.checked == true) {
    elementToHide.style.display = "block";
  } else {
    elementToHide.style.display = "none";
  }
}