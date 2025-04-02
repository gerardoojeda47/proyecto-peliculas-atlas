function agregarGenero() {

    const genero ={ nombre: document.getElementById("txtGenero").value} 
    const url = "/generos/"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(genero)
    })
    .then(respuesta => respuesta.json())
    .then(data => {
        if (data.status == 200) {
            location.href = "/generos/"
        } else {
            swal.fire("Error", data.message, "error")
            alert("Error al agregar el genero")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al agregar el genero")
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
            // Redirigir a la página de listar películas después de 2 segundos
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
    .then(respuesta => {

        console.log("respuesta", respuesta)
        if (!respuesta.ok) {
            throw new Error("Error en la respuesta del servidor");
        }
        return respuesta.json()
    } )
    .then(resultado => {
        console.log("esta es la data; ", resultado)
        if (resultado.message == "Inicio de sesión exitoso") {
            swal.fire("Iniciando Sesion", resultado.message, "success")
            setTimeout(function() {
                location.href = "/dash"
            },2000)
        } else {
            swal.fire("Error", resultado.message, "error")
            alert("Error al iniciar sesión")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al iniciar sesión")
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
    .then(data => {
        if (data.message == "Pelicula actualizada") {
            location.href = "/listarPeliculas"
        } else {
            swal.fire("Error", data.message, "error")
            alert("Error al editar la pelicula")
        }
    })
    .catch(error => {
        console.log(error)
        alert("Error al editar la pelicula")
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