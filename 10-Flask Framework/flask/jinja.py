from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to home page</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

#Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "The marks you got is "+str(score)

#Jinja2 template
@app.route('/sucess/<int:score>')
def sucess(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

@app.route('/sucessres/<int:score>')
def sucessres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'Score':score,'Res':res}
    return render_template('result1.html',result=exp)


# Dynamic URL
@app.route('/submitt', methods=['GET', 'POST'])
def submitt():

    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + c + datascience) / 4

        return redirect(url_for('sucessres', score=total_score))

    return render_template('submitt.html')

if __name__=="__main__":
    app.run(debug=True)