# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask("Financial Transactions")

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation -- implemented before other functions to be able to redirect the page with all transactions every time a new transaction is created, updated, or deleted
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions = transactions)

# Create operation
@app.route('/add', methods = ["GET", "POST"])
def add_transaction():  
    if request.method == "POST":
        # retrieve data from form
        DATE = request.form['date']
        AMOUNT = request.form['amount']
        
        # create NEW_TRANSACTION object using form data
        NEW_TRANSACTION = {
            'id': len(transactions)+1,
            'date': DATE,
            'amount': float(AMOUNT)
            }
        
        # Append the new transaction to the transactions list page
        transactions.append(NEW_TRANSACTION)

        # redirect to the transactions list page
        return redirect(url_for("get_transactions"))
    
    # render the form template to display the add transaction form
    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        # extract updated values from the form fields
        DATE = request.form['date']
        AMOUNT = float(request.form['amount'])

        # iterate through transactions to find the transaction with the matching ID and update the date and amount fields
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = DATE
                transaction['amount'] = AMOUNT
                break

        # redirect to the transactions list page
        return redirect(url_for("get_transactions"))

    # iterate through transactions to find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # iterate through the transactions to find the transaction with the matching ID, and delete the transaction with the given ID
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    
    # redirect to the transactions list page
    return redirect(url_for("get_transactions"))

# Search operation
@app.route('/search', methods = ["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        # retrieve maximum and minimum values from form
        MAX_AMOUNT = float(request.form['max_amount'])
        MIN_AMOUNT = float(request.form['min_amount'])

        # create empty list to filter transactions
        filtered_transactions = []

        # iterate through transactions. If the amount in the transaction element is greater than the min and less than the max, add this element to the filtered_transactions list
        for transaction in transactions:
            if transaction["amount"] > MIN_AMOUNT: 
                if transaction["amount"] < MAX_AMOUNT:
                    filtered_transactions.append(transaction)

        # render transactions page using the filtered_transactions list
        return render_template('transactions.html', transactions = filtered_transactions)

    # render search page
    return render_template('search.html')

# Total balance: calculate and display the total balance of all transactions
@app.route('/balance')
def total_balance():
    total = 0
    for transaction in transactions:
        total = total + transaction['amount']

    return render_template('transactions.html', transactions = transactions, total = total)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug = True)
