let checkButton = document.getElementById('checkBtn');
let clearButton = document.getElementById('clearBtn');
let result = document.getElementById('result');

checkButton.addEventListener('click', function() {
    let input = document.getElementById('textarea').value;
    if (input === '') {
        alert('Please enter a number.');
        return;
    }
});

clearButton.addEventListener('click',function(){
    document.getElementById('textarea').value = '';
    result.innerHTML = ''; 
    result.style.display = 'none';
})