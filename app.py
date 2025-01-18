from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for expenses
expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    description = data.get('description')
    amount = data.get('amount')
    date = data.get('date')

    if not description or not amount or not date:
        return jsonify({'error': 'All fields are required!'}), 400

    expense = {'description': description, 'amount': float(amount), 'date': date}
    expenses.append(expense)
    return jsonify({'message': 'Expense added successfully!'})

@app.route('/get_expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

@app.route('/get_total', methods=['GET'])
def get_total():
    total = sum(expense['amount'] for expense in expenses)
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(debug=True)
