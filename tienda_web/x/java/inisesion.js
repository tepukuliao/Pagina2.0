function validar(){
  var user = document.getElementById("user").value;
  if(user === ""){
    document.getElementById("mensajeUser").textContent = "porfavor ingrese nombre de usuario"
  }else{
    document.getElementById("mensajeUser").textContent = ""
  }

  var pass = document.getElementById("pass").value;
  if(pass === ""){
    document.getElementById("mensajePass").textContent = "porfavor ingrese contraseña"
  }else{
    document.getElementById("mensajePass").textContent = ""
  }
}




