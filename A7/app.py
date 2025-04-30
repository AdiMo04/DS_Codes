from flask import Flask, request, render_template
import requests  # For sending HTTP requests to backend API

app = Flask(__name__)

# Route for home page that handles both GET and POST
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get form inputs and convert to integers
        a = int(request.form['a'])
        b = int(request.form['b'])
        op = request.form['op']  # Operation selected by user

        # Send POST request to backend API server with operation and operands
        result = requests.post(f"http://localhost:5000/{op}", json={"a": a, "b": b}).text

        # Display result and back link
        return f"Result: {result}<br><br><a href='/'>Go Back</a>"

    # For GET request, render the form page
    return render_template("index.html")

# Start the app on port 3000 (frontend)
app.run(port=3000)




#1: in new terminal : python api.py
#2: in new terminal : python app.py
#3: Then open: http://localhost:3000 in your browser.