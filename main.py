from flask import Flask, request , render_template

app=Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    a=5
    b=7
    result=a+b
    return render_template("index.html",result=result)
def info():
    
    return "hi i'm info page"


if __name__=="__main__":
    app.run()