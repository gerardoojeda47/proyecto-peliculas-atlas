function agregarGenero() {
    console.log("ingreso  ala funcion agregargenero");
    const genero ={ nombre: document.getElementById("txtGenero").value} 
    const url = "/generos"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(genero)
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        if (resultado.message) {
            swal.fire("Agregar género", resultado.message, "success")
            setTimeout(function() {
                location.href = "/generosVista"
            },2000)
        } else {
            swal.fire("Error", resultado.message, "error")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al agregar el género")
    })
}

function agregarPelicula() {
    url="/addPelicula"
    const protagonistasInput = document.getElementById("txtProtagonistas").value;
    const protagonistasArray = protagonistasInput.split(",").map(pro => pro.trim());
    const pelicula = {
        codigo: document.getElementById("txtCodigo").value,
        titulo: document.getElementById("txtTitulo").value,
        duracion: document.getElementById("txtDuracion").value,
        protagonistas: protagonistasArray,
        resumen: document.getElementById("txtResumen").value,
        genero: document.getElementById("cbGenero").value
    }
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pelicula)
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        console.log(resultado)
        if (resultado.message) {
            swal.fire("Agregar Pelicula", resultado.message, "success")
            setTimeout(function() {
                location.href = "/listarPeliculas"
            },2000)
        } else {
            swal.fire("Agregar Pelicula", data.message, "error")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al agregar la pelicula" )
    })
}

function login() {
    const usuario = document.getElementById("txtUser").value.trim()
    const passwordIn = document.getElementById("txtPassword").value.trim()

    // Validar que los campos no estén vacíos
    if (!usuario || !passwordIn) {
        swal.fire("Error", "Por favor, completa todos los campos", "error");
        return;
    }

    const url = "/usuarios/login"
    const loginData = {
        userId: usuario,
        password: passwordIn
    }
    console.log("datos enviados", loginData);
 
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(respuesta =>  respuesta.json())  
    .then(resultado => {
        console.log("esta es la data; ", resultado.message)
        if (resultado.message == "Inicio de sesión exitoso") {
            swal.fire("Iniciando Sesion", resultado.message, "success")
            setTimeout(function() {
                location.href = "/dash"
            },2000)
        } else {
            if (resultado.message == "Contraseña incorrecta") {
                swal.fire("Error", resultado.message, "error")
                alert("Contraseña incorrecta")
            } else if (resultado.message == "Usuario no encontrado") {
                swal.fire("Error", resultado.message, "error")
                alert("Usuario no encontrado")
            }
            swal.fire("Error", resultado.message, "error")
            // alert("Error al iniciar sesión", resultado.message)
        }
    })
    .catch(error => {
        console.log("el error es: ", error)
        alert("Error al iniciar sesión del catch") 
    })
}

function salir(){
    const url = "/usuarios/logout"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(respuesta => respuesta.json())
    .then(resultado => {
        console.log("esta es la data; ", resultado)
        if (resultado.message == "Sesión cerrada") {
            location.href = "/loginVista"
            alert("Sesion cerrada")
        } else {
            swal.fire("Error", resultado.message, "error")
            alert("Error al cerrar la sesion")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al cerrar la sesion")
    })
}

function editarPelicula(codigo) {
    const url = "/peliculas/" + codigo
    const protagonistasInput = document.getElementById("txtProtagonistas").value;
    const protagonistasArray = protagonistasInput.split(",").map(pro => pro.trim());
 
    const pelicula = {
        codigo: document.getElementById("txtCodigo").value,
        titulo: document.getElementById("txtTitulo").value,
        duracion: document.getElementById("txtDuracion").value,
        protagonistas: protagonistasArray,
        resumen: document.getElementById("txtResumen").value,
        genero: document.getElementById("cbGenero").value
    }
    console.log("datos enviados", pelicula);
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pelicula)
    })
    .then(respuesta => respuesta.json())
    
    .then(resultado => {
        console.log("esta es la data; ", resultado)
        if (resultado.message == "Pelicula actualizada") {
            location.href = "/listarPeliculas"
        } else {
            swal.fire("Error", resultado.message, "error")
            alert("Error al editar la pelicula")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al editar la pelicula del catch")
    })
}

function actualizarGenero(codigo) {
    const url = "/generos/" + codigo
    const genero = {
        nombre: document.getElementById("txtGenero").value
    }
    fetch(url, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(genero)
    })
    .then(respuesta => respuesta.json())
    .then(data => {
        if (data.message == "Genero actualizado") {
            location.href = "/generosVista"
        } else {
            swal.fire("Error", data.message, "error")
            alert("Error al actualizar el genero")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al actualizar el genero")
    })
}

//otra forma de hacerlo mediante JS
// function eliminarPelicula(codigo) {
//     const url = "/peliculas/" + codigo
//     fetch(url, {
//         method: 'DELETE',
//         headers: {
//             'Content-Type': 'application/json'
//         }
//     })
//     .then(respuesta => respuesta.json())
//     .then(data => {
//         if (data.message == "Pelicula eliminada") {
//             location.href = "/listarPeliculas"
//         } else {
//             swal.fire("Error", data.message, "error")
//             alert("Error al eliminar la pelicula")
//         }
//     })
//     .catch(error => {
//         console.log(error)
//         alert("Error al eliminar la pelicula")
//     })
// }