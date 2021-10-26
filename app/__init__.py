from flask import *
from datetime import *
app = Flask(__name__)

ministers = ["ScoMo", "Turnbull", "Julia"]

@app.route("/")
def main():
    if "time_started" in session:
        return render_template("template.html",
                               time=session["time_started"])
    else:
        return render_template("template.html")

@app.route("/start_session")
def start_session():
    if "time_started" not in session:
        right_now = datetime.now()
        time_formatted = right_now.strftime("%A, %d %B %Y, %H:%M:%S")
        session["time_started"] = time_formatted
    return redirect("/")

@app.route("/stop_session")
def stop_session():
    if "time_started" in session:
        session.pop("time_started")
    return redirect("/")
    return render_template("template.html")
    
@app.route("/post_input", methods=["POST"])
def post_input():
    message = request.form["myInput"]
    return render_template_string(message)

@app.route("/get_input", methods=["GET"])
def get_input():
    message = request.args.get("myInput")
    return render_template_string(message)

@app.route("/contact")
def contact():
    return "Contact page."
 
app.run(debug=True)