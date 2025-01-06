// Add click event listeners to all close buttons
document.querySelectorAll('.alert-close').forEach(button => {
    button.addEventListener('click', function() {
        const alert = this.closest('.custom-alert');
        alert.classList.add('alert-fade-out');
        setTimeout(() => {
            alert.classList.add('alert-hidden');
            alert.classList.remove('alert-fade-out');
        }, 300);
    });
});

// Function to show alerts
function showAlert(type) {
    const alerts = document.querySelectorAll('.custom-alert');
    alerts.forEach(alert => {
        if (alert.classList.contains(`alert-${type}`)) {
            alert.classList.remove('alert-hidden');
        } else {
            alert.classList.add('alert-hidden');
        }
    });
}

// Initially hide all alerts
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.custom-alert').forEach(alert => {
        alert.classList.add('alert-hidden');
    });
});


document.addEventListener('DOMContentLoaded', function() {
    // Select the close button
    const closeButton = document.querySelector('.alert-close');

    // Add click event listener to the close button
    closeButton.addEventListener('click', function() {
        // Select the alert container and hide it
        const alertContainer = document.querySelector('.alert-container');
        alertContainer.style.display = 'none';
    });
});