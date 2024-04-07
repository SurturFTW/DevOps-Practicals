from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the numbers from the form
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    num3 = float(request.form['num3'])
    # Perform calculations
    total = num1 + num2 + num3
    average = total / 3
    product = num1 * num2 * num3
    # Render the template with the result
    return render_template('result.html', total = total, average = average, product = product)
# Run the Flask app using the built-in development server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
