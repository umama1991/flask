from flask import Flask,render_template

app=Flask(__name__)
#Homepage
@app.route("/")
def home(): #decorator
    return "hello flask"
# @app.route("/about")
# def about(): #decorator
#     return "welcome to about page"
@app.route("/about<name>")
def about(name): 
     return f"welcome mr. {name} to about page"
@app.route("/contact")
def contact(): #decorator
     return render_template("contact.html")

if __name__ =="__main__":
    app.run(debug=True) #agar app disturb ho to error ko check kr sakain


