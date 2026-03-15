"""
ASSIGNMENT 11:
Module 19: Flask- Registration form project

Submission: You need to upload the compressed zip file of your working project folder to drive and then submit the accessible link (make sure to enable sharing access).
Reference: For reference, as mentioned above, please follow Python course >Module 19.

Note: You can always connect to the mentor using the chat support option for any doubts or queries!

"""


from flask import Flask, render_template, request, redirect, url_for

# Interaction
webpage = Flask(__name__)

# Home / Register Page
@webpage.route('/')
@webpage.route('/register')
def homepage():
    return render_template('register.html')


# Confirmation Page
@webpage.route("/confirmation", methods=['POST'])
def register():

    # Basic Personal Information
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Contact Information
    mobile = request.form.get('mobile')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    pincode = request.form.get('pincode')

    # Personal Details
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    nationality = request.form.get('nationality')

    # Academic Information
    course = request.form.get('course')
    department = request.form.get('department')
    rollnumber = request.form.get('rollnumber')
    college = request.form.get('college')

    # Security Fields
    security_question = request.form.get('security_question')
    security_answer = request.form.get('security_answer')

    return render_template(
        'confirm.html',
        firstname=firstname,
        lastname=lastname,
        username=username,
        email=email,
        mobile=mobile,
        address=address,
        city=city,
        state=state,
        pincode=pincode,
        dob=dob,
        gender=gender,
        nationality=nationality,
        course=course,
        department=department,
        rollnumber=rollnumber,
        college=college,
        security_question=security_question,
        security_answer=security_answer
    )


# Main
if __name__ == "__main__":
    webpage.run(debug=True)