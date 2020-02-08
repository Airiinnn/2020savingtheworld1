from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", valid=True)
    else:
        scale = request.form.get("scale")
        temp = request.form.get("temp")
        if not temp.isdigit():
            return render_template("index.html", valid=False)

        temp = float(temp)
        
        if scale == "F":
            temp = round(((temp - 32) * 5 / 9), 1)
            
        if temp >= 38.0:
            risk = "High"
        else:
            risk = "Low"
        
        return render_template("index.html", valid=True, temp=temp, scale=scale, risk=risk)
        
if __name__ == "__main__":
    app.run(debug=True)