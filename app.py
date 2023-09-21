from flask import Flask,render_template,request


app=Flask(__name__)
#Homepage
@app.route("/")
def home(): #decorator
    return render_template("home1.html")

@app.route("/about")
def about(): #decorator
    return render_template("about.html")
# @app.route("/about<name>")
# def about(name): 
#      return f"welcome mr. {name} to about page"

@app.route("/contact")
def contact(): #decorator
     return render_template("contact.html")

@app.route("/gallery")
def gallery(): 

     return render_template("gallery.html")

@app.route("/form",methods=['GET','POST'])
def form(): 
     if request.method=='GET':
        return render_template1("home1.html")
     else:
         math=float(request.form['maths'])
         science=float(request.form['science'])
         history=float(request.form['history'])
         average =(math+science+history)/3
     return render_template("home1.html",score=average)
if __name__ =="__main__":
    app.run(debug=True) #agar app disturb ho to error ko check kr sakain


