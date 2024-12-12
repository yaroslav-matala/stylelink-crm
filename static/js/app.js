
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

window.onload = function () {
    const testimonials = document.getElementById("testimonials");
    testimonials.scrollLeft = 0; // Adjust the value to set the offset
};