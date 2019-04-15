from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():

    username = ""
    email = ""
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""
    

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        verify_password = request.form["verify"]
        email = request.form["email"]

        #verify username has no spaces and is correct length
        for i in username:
            if i.isspace():
                username_error = "Username cannot contain spaces!"
                username = ""
            else:
                if (len(username) < 3) or (len(username) > 20):
                    username_error = "Username needs to be between 3 and 20 characters!"
                    username = ""

        if username == "":
            username_error = "Not a valid username!"
            username = ""

        #verify password has no spaces and is correct length
        for i in password:
            if i.isspace():
                password_error = "Password must not contain spaces!"
            else:
                if (len(password) < 3) or (len(password) > 20):
                    password_error = "Password must be between 3 and 20 characters and not contain spaces!"
        if password == "":
            password_error = "You must enter a password!"

        #verify password matches verify_password
        if password != verify_password:
            verify_password_error = "Passwords do not match!"

        if (email != "") and ("@" not in email) and ("." not in email) :
            email_error = "This is not a valid email."
            email = ""

        if (not username_error) and (not password_error) and (not verify_password_error) and (not email_error):
            return redirect("/welcome?username={0}".format(username))

    return render_template("index.html")


@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome-page.html", username=username)


if __name__ == "__main__":
    app.run()