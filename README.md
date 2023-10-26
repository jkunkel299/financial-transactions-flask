# Financial Transactions Application

This is a web application developed using Python in the Flask microframework. The application allows display and manipulation of transaction data using CRUD operations.

## Details

The application has four different web pages. 

The Transaction Records page displays all the transactions entries created in the system. This page gives an option to Edit and Delete the available entries, as well as the option of adding a new entry. 
When the '/balance' route is called in the URL, this page will also display the total balance of all transactions. 

The Add Transaction page is used when the user chooses to add the entry on the previous page (Transaction Records). The user adds the Date and Amount values for the new entry, then is redirected to the Transaction Records page, where their entry has been added to the list of transactions. 

The Edit Transaction page is used when the user clicks the edit entry option on the Transaction Records page. The user can edit the Date and Amount values for the selected entry, then is redirected to the Transaction Records page, where the chosen entry has been updated.

The Search page is used when the user includes '/search' in the URL. This page allows the user to input a minimum and maximum transaction value, then returns a filtered list of transactions.

## Requirements
This web application uses the Flask microservice. The Flask package must be installed.
```bash
pip install Flask
```
