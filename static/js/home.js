document.getElementById("dropdown").addEventListener("change", function() {
    var selectedOption = this.value;
    if (selectedOption) {
      window.location.href = selectedOption;
    }
  });
  document.getElementById("urlSelect").addEventListener("change", function() {
    var selectedOption = this.value;
    if (selectedOption) {
      window.location.href = selectedOption;
    }
  });