from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    result = None
    if request.method == 'POST':
        operation = request.form.get('operation')

        # Uppercase converter
        if operation == 'uppercase':
            text = request.form.get('text', '')
            result = text.upper()

        # Area of circle
        elif operation == 'circle':
            try:
                radius = float(request.form.get('radius', 0))
                result = 3.1416 * radius * radius
            except ValueError:
                result = "Invalid input."

        # Area of triangle
        elif operation == 'triangle':
            try:
                base = float(request.form.get('base', 0))
                height = float(request.form.get('height', 0))
                result = 0.5 * base * height
            except ValueError:
                result = "Invalid input."

    return render_template('works.html', result=result)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)
