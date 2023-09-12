from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'the very secret key'
    
@app.route('/')

def counter():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count']+= 1
    return render_template("index.html",)  

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

@app.route('/addtwo')
def add_two():
    session['count'] += 2
    return render_template("index.html")

@app.route("/plus", methods = ['POST'])
def plus():
    # session['count'] += int(request.form['visit'])
    return redirect(f'/{request.form["visit"]}')

@app.route("/<int:num>") 
def increment(num):
    session['count'] += num
    return render_template('index.html')



if __name__=="__main__":      
    app.run(debug=True)