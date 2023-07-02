const foodForm = document.querySelector('#food-form');
const nameInput = document.querySelector('#name');
const countryInput = document.querySelector('#country');
const typeInput = document.querySelector('#type');
const priceInput = document.querySelector('#price');
const errorMessage = document.querySelector('#error-message');

foodForm.addEventListener('submit', (event) => {
    // Regular expressions for validation
    const nameRegex = /^[a-zA-Z]+$/;
    const countryRegex = /^[a-zA-Z]+$/;
    const typeRegex = /^[a-zA-Z1-9\-]+$/;
    const priceRegex = /^\d+$/;

    // Array to store error messages
    let errors = [];

    // Check if name input is valid
    if (!nameRegex.test(nameInput.value)) {
        errors.push('Name must only contain letters.');
    }

    // Check if department input is valid
    if (!countryRegex.test(countryInput.value)) {
        errors.push('Country must only contain letters.');
    }

    // Check if role input is valid
    if (!typeRegex.test(typeInput.value)) {
        errors.push('Type must only contain letters.');
    }

    // Check if salary input is valid
    if (!priceRegex.test(priceInput.value) || parseInt(priceInput.value) < 5) {
        errors.push('Price must be a number greater than or equal to 5.');
    }

    // Prevent form from submitting if there are any errors
    if (errors.length > 0) {
        event.preventDefault();

        // Set error message and style
        errorMessage.innerHTML = errors.join('<br>');
        errorMessage.style.color = 'red';
    } else {
        // Clear error message if validation passes
        errorMessage.textContent = '';
    }
});
