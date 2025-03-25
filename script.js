let checkButton = document.getElementById('checkBtn');
let clearButton = document.getElementById('clearBtn');
let result = document.getElementById('result');


//function for loader to show
function showLoader() {
    loader.style.display = 'block';
}

//function for loader to hide 
function hideLoader() {
    loader.style.display = 'none';
}


//function to show the input text is human writtten or ai written
checkButton.addEventListener('click', function() {
    showLoader();
    let input = document.getElementById('textarea').value;
    if (input === '') {
        alert('Please enter a number.');
        return;
    }
    //fetching the data from the api
    fetch(`${apiUrl}?q=${input}&app_id=86a48720&app_key=${apiKey}`)
    .then(response => response.json())
    .then(data => {
      displayResult(data.hits);
      hideLoader(); 
    })
    .catch(error => {
      console.error('Error fetching data:', error);
      hideLoader(); 
      alert("enter correctly")
    });
});

//function to clear the input field
clearButton.addEventListener('click',function(){
    document.getElementById('textarea').value="";
    result.innerHTML="";
    result.style.display = 'none';
});


//function to display the result
function displayResult(result) {
    result.innerHTML = '';
  
    result.forEach(results => {
      const { label } = results.results;

      
      const resultCard = document.createElement('div');
      resultCard.classList.add('resultCard');
  
      const resultPredict = document.createElement('h2');
      resultPredict.textContent = label;
  
  
      resultCard.appendChild(resultCard);
      resultPredict.appendChild(resultPredict);
      resultCard.appendChild(resultCard);
    });
  }
  
hideLoader();