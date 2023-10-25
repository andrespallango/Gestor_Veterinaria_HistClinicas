document.addEventListener('DOMContentLoaded', function () {
    // Obtenemos una referencia al formulario
    const form = document.querySelector('form');

    // Asociamos un evento al formulario para validar los campos antes de enviar el formulario
    form.addEventListener('submit', function (event) {
        // Obtenemos una referencia a todos los campos de entrada de texto
        const inputFields = document.querySelectorAll('.validate-input');

        let hasEmptyFields = false;
        inputFields.forEach(function (input) {
            if (input.value === '') {
                hasEmptyFields = true;
            }
        });

        if (hasEmptyFields) {
            event.preventDefault();
            alert('Por favor, llena todos los campos obligatorios.');
        }
    });
});
