let checkButton = document.getElementById('checkBtn');
let clearButton = document.getElementById('clearBtn');
let result = document.getElementById('result');

checkButton.addEventListener('click', function() {
    let input = document.getElementById('textarea').value;
    if (input === '') {
        alert('Please enter a number.');
        return;
    }
        // Simulate checking the text (replace this with actual logic)
        let isHumanWriting = Math.random() < 0.5; // Randomly decide for demo purposes
        result.innerHTML = isHumanWriting ? 'This text is likely human writing.' : 'This text is likely AI writing.';
        result.style.display = 'block';

    
});

