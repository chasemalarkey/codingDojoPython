from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')
# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def say(name):
    return "Hello, " + name
@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return render_template("repeat.html", num=num, word=word)
# if not success() or dojo() or say() or repeat():
#     print("Sorry! No response. Try again.")
# app.run(debug=True) should be the very last statement! 

# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

