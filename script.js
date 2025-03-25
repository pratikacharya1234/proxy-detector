// Get DOM elements
let checkButton = document.getElementById('checkBtn');
let clearButton = document.getElementById('clearBtn');
let result = document.getElementById('result');
let loader = document.getElementById('loader'); // Assuming loader has an ID in HTML

// Function to show loader
function showLoader() {
    loader.style.display = 'block';
}

// Function to hide loader
function hideLoader() {
    loader.style.display = 'none';
}

// Check button logic to detect AI vs human text
checkButton.addEventListener('click', function() {
    showLoader();
    let input = document.getElementById('textarea').value;
    
    // Validate input
    if (input === '') {
        alert('Please enter some text.');
        hideLoader(); 
        return;
    }

    // Fetch data from Flask API
    fetch('http://localhost:5000/detect', {
        method: 'POST',
        body: JSON.stringify({ text: input }), 
        headers: { 'Content-Type': 'application/json; charset=UTF-8' }
    })
    // Parse JSON response
    .then(response => response.json()) 
    .then(data => {
        // Pass Flask response to display function
        displayResult(data); 
        hideLoader();  
    })
    .catch(error => {
        console.error('Error fetching data:', error);
        result.innerHTML = 'Error: Could not analyze text.';
        result.style.display = 'block'; 
        hideLoader(); 
    });
});

// Clear button logic
clearButton.addEventListener('click', function() {
    document.getElementById('textarea').value = '';
    result.innerHTML = '';
    result.style.display = 'none';
});

// Function to display the result
function displayResult(data) {
    result.innerHTML = ''; 

    // Extract result and confidence from Flask response
    const prediction = data.result || 'Unknown';
    const confidence = data.confidence || 0;

    // Create result card
    const resultCard = document.createElement('div');
    resultCard.classList.add('resultCard');

    // Create prediction text
    const resultPredict = document.createElement('h2');
    resultPredict.textContent = `${prediction} (${(confidence * 100).toFixed(2)}% confidence)`;

    // Append elements correctly
    resultCard.appendChild(resultPredict);
    result.appendChild(resultCard);
    
    result.style.display = 'block';
}

hideLoader();