from flask import Flask, render_template, request
from linkedlist import LinkedList
from infixpostfix import infix_to_postfix 

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


linked_list = LinkedList()

@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    result = ""
    list_state = linked_list.display()

    if request.method == 'POST':
        action = request.form.get('action')
        value = request.form.get('value')

        if action == 'insert_beginning':
            result = linked_list.insert_at_beginning(value)
        elif action == 'insert_end':
            result = linked_list.insert_at_end(value)
        elif action == 'remove_beginning':
            result = linked_list.remove_beginning()
        elif action == 'remove_end':
            result = linked_list.remove_end()
        elif action == 'remove_value':
            result = linked_list.remove_value(value)
        elif action == "search":
            if value:
                result = linked_list.search(value)
            else:
                result = "Please enter a value to search."
            
        list_state = linked_list.display()

    return render_template('linkedlist.html', result=result, list_state=list_state)

@app.route('/infixpostfix', methods=['GET', 'POST'])
def infixpostfix():
    result = None
    error = None
    if request.method == 'POST':
        expression = request.form.get('expression', '').strip()
        if expression:
            try:
                result = infix_to_postfix(expression)
            except Exception as e:
                error = f"⚠️ Invalid input: {str(e)}"
        else:
            error = "⚠️ Please enter an expression."
    return render_template('infixpostfix.html', result=result, error=error)

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        text = request.form.get('inputString', '')
        result = text.upper()
    return render_template('toUppercase.html', result=result)

@app.route('/areaofcircle', methods=['GET', 'POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', 0))
            result = 3.1416 * radius * radius
        except ValueError:
            result = "Invalid input."
    return render_template('AreaOfCircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            height = float(request.form.get('height', 0))
            result = 0.5 * base * height
        except ValueError:
            result = "Invalid input."
    return render_template('AreaOfTriangle.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
