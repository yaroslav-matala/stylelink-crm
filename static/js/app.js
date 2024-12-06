
// message timer

let message_timeout = document.getElementById("message-timer");

setTimeout(function() {
    if (message_timeout) {
        message_timeout.style.display = "none";
    }
}, 5000);

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to make rows clickable
    document.querySelectorAll('.clickable-row').forEach(row => {
        row.addEventListener('click', function() {
            window.location = this.getAttribute('data-href');
        });
    });
});