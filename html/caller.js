document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    
    var formData = new FormData(this);

    // Send AJAX request
    fetch('/register', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        
        alert(data.message);
        if (data.success) {
            window.location.href = '/login.html'; 
        }
    })
    .catch(error => console.error('Error:', error));
});


document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    
    var formData = new FormData(this);

    // Send AJAX request
    fetch('/login', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        
        alert(data.message);
        if (data.success) {
            window.location.href = '/profile'; 
        }
    })
    .catch(error => console.error('Error:', error));
});

