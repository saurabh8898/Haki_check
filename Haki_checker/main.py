from flask import Flask, request, render_template

app = Flask(__name__)

# Display the question page
@app.route('/')
def question():
    return render_template('questions.html')  # This will serve the HTML page you created

# Handle form submission
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form['answer']  # Get the selected option from the form
    # Save the answer, for example in a file, database, or for further processing
    with open('answers.txt', 'a') as f:
        f.write(f"Selected answer: {answer}\n")
    return f"Your answer {answer} has been submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
