import { questions } from './questions.js';

let currentQuestionIndex = 0;

document.getElementById('start-button').onclick = () => {
    displayQuestion(currentQuestionIndex);
    currentQuestionIndex++;
    // Hide the start button after starting
    document.getElementById('start-button').style.display = 'none';
};

function displayQuestion(index) {
    const questionElement = document.getElementById('question');
    const optionsElement = document.getElementById('options');

    // Clear previous options
    optionsElement.innerHTML = '';

    if (index < questions.length) {
        const currentQuestion = questions[index];
        questionElement.textContent = currentQuestion.question;

        currentQuestion.options.forEach(option => {
            const button = document.createElement('button');
            button.textContent = option.text;
            button.className = 'option-button';
            button.value = option.value;
            button.onclick = () => handleOptionClick(option.value);
            optionsElement.appendChild(button);
        });
    } else {
        questionElement.textContent = 'No more questions!';
        // Optionally, show a message or restart button here
    }
}

function handleOptionClick(value) {
    console.log('Selected option value:', value);
    // Handle the selected option here
    // You might want to store the answers or proceed to the next question
    currentQuestionIndex++;
    displayQuestion(currentQuestionIndex);
}
