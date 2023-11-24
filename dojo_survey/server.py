from flask import Flask, render_template, redirect, session, request # Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def survey():
    return render_template('index.html') 


@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')
@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

