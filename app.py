from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        scale = request.form.get("scale")
        temp = request.form.get("temp")
        temp = float(temp)
        
        if scale == "f":
            temp = round(((temp - 32) * 5 / 9), 1)
            
        if temp >= 38.0:
            risk = "high"
        else:
            risk = "low"
        
        return render_template("index.html", temp=temp, scale=scale, risk=risk)
        
if __name__ == "__main__":
    app.run(debug=True)