document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("miFormulario");
    form.addEventListener("submit", e => {
        e.preventDefault(); // Eliminamos el comportamiento por defecto del formulario

        // Obteniendo los valores ingresados por los inputs
        let textoNombre = document.getElementById("nombre").value;
        let textoCorreo = document.getElementById("correo").value;

        // Expresion regular formato GMAIL.COM
        let verificarFormatoCORREO = /@gmail.com$/;
        let verificandoCO = verificarFormatoCORREO.test(textoCorreo);

        // Borrando los espacios en blanco con función TRIM
        let nombreTrim = textoNombre.trim();
        document.getElementById("nombre").value = nombreTrim;

        // Condicionando los valores ingresados por el cliente
        if (nombreTrim === '') {
            let advertencia = "Ingrese su nombre.";
            document.getElementById('validar').textContent = advertencia;
            document.getElementById("nombre").focus();
        } else if (!verificandoCO) {
            let advertencia = "El Correo " + textoCorreo + " no es válido.";
            document.getElementById('validar').textContent = advertencia;
            document.getElementById("correo").focus();
        } else {
            let advertencia = "¡Los datos han sido enviados correctamente!";
            document.getElementById('validar').textContent = advertencia;
            alert("Datos del formulario enviados");

            // Enviar el formulario después de la validación
            form.submit();
        }
    });
});