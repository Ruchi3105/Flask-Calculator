from flask import Flask, request, render_template
import math

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def calc():
    expression=""
    result=""
    if request.method=='POST':
        expression = request.form['expression']
        if request.form['submit']=='AC':
            expression=""
            result=""
        elif request.form['submit']=='⌫':
            expression=expression[:-1]
        elif request.form['submit']=='=':
            try:
                if "sqrt" in expression:
                    expression=expression.replace("sqrt","math.sqrt")
                result=eval(expression)
            except Exception as e:
                result="Error"
        else:
            expression+=request.form["submit"]
            
    return render_template('index.html', expression=expression, result=result)

if __name__=='__main__':
    app.run(debug=True)