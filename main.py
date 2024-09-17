from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the QuestionAnswer model
class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(100), nullable=False)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

# Route for the question page
@app.route('/question')
def question():
    return render_template('question.html')
#Route to second question page
@app.route('/question2')
def question2():
    return render_template('question2.html')

#Route to third question page
@app.route('/question3')
def question3():
    return render_template('question3.html')

#Route to fourth question page
@app.route('/question4')
def question4():
    return render_template('question4.html')

#Route to fifth question page
@app.route('/question5')
def question5():
    return render_template('question5.html')

#Route to Sixth question page
@app.route('/question6')
def question6():
    return render_template('question6.html')

#Route to Seventh question page
@app.route('/question7')
def question7():
    return render_template('question7.html')

#Route to Eight question page
@app.route('/question8')
def question8():
    return render_template('question8.html')

#Route to Ninth question page
@app.route('/question9')
def question9():
    return render_template('question9.html')

#Route to Tenth question page
@app.route('/question10')
def question10():
    return render_template('question10.html')

#Route to Eleventh question page
@app.route('/question11')
def question11():
    return render_template('question11.html')

#Route to Twelth question page
@app.route('/question12')
def question12():
    return render_template('question12.html')

#Route to Thirteenth question page
@app.route('/question13')
def question13():
    return render_template('question13.html')

#Route to fourteen question page
@app.route('/question14')
def question14():
    return render_template('question14.html')

#Route to Fifteen question page
@app.route('/question15')
def question15():
    return render_template('question15.html')


# Route to handle the form submission using AJAX
@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    answer = request.form.get('answer')
    if answer:
        # Save the answer in the database
        new_entry = QuestionAnswer(answer=answer)
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'status': 'success'})
    return jsonify({'status': 'error'})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
