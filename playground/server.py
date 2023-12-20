from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def display_boxes():
    return render_template("index.html", num = 3)  
@app.route('/play/<int:num>')
def display_num_boxes(num):
    return render_template("index.html", num=num)
@app.route('/play/<int:num>/<string:color>')
def display_color(num, color):
    return render_template("index.html", num=num, color=color)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

