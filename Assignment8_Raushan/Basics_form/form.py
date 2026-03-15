#import
from flask import Flask, render_template, request

# Interaction
webpage =Flask(__name__)

# Mapping
@webpage.route('/')
@webpage.route('/register')

# Inputs
def homepage():
    return render_template('register.html')

@webpage.route("/confirmation", methods = ['POST','GET'])
#inputs
def register():
    if request.method == "POST":
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone number')
        return render_template('confirm.html',name =n, city=c, phonenumber = p )



# Main
if __name__ == "__main__":
    webpage.run(debug=True)

#