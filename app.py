from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    link = "<h1>歡迎來到吳冠頡的網站</h1>"
    link +="<a href=/index>自我介紹</a><hr>"
    link +="<a href=/resume>履歷</a><hr>"
    link +="<a href=/work>工作介紹</a><hr>"
    link +="<a href=/hobby>職能診段結果</a><hr>"
    link +="<a href=/ucan>何倫碼</a><hr>"
    return link    

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/hobby")
def hobby():
    return render_template("hobby.html")

@app.route("/ucan")
def ucan():
    return render_template("ucan.html")

if __name__ == "__main__":
    app.run(debug=True)