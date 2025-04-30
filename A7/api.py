from flask import Flask, request

app = Flask(__name__)

# API endpoint that handles POST requests for various operations
@app.route("/<op>", methods=["POST"])
def calc(op):
    d = request.json  # Parse incoming JSON body
    a, b = d['a'], d['b']  # Extract operands

    # Perform operation using dictionary mapping
    return str({
        'add': a + b,
        'sub': a - b,
        'mul': a * b,
        'div': a / b
    }[op])  # Lookup based on URL path (op)

# Start backend API on default port 5000
app.run()




#1: python api.py
#2: python app.py
#3: Then open: http://localhost:3000 in your browser.