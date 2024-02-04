This Jupyter workbook is meant to help an organization on Open Collective reconcile the transactions on Wise, Stripe, Paypal and bank accounts with transactions on Open Collective.
Documentation for the script is included in the reconciliation_pipeline.ipynb workbook. 

After running the workbooks you will end up with a number of CSVs in /reports/your_fiscal_host/. These CSVs include all transactions from Wise, Stripe, Paypal and banks that were loaded in the script, matched to their corresponding transactions on the platform or on the bank.

## How to use the output from this workbook

This workbook produces new CSV files that merge the transaction rows from the different merchant platforms and bank accounts to the platform transaction they correspond to. These files can be used for accounting purposes to connect transactions on the merchant accounts with their corresponding platform activity. All output files have the column "_reconciliation_category" that contains a guiding comment for understanding the nature of the transaction.

Some transactions haven been reconciled between a bank account and a merchant account. Examples of such transactions are balance transfers between accounts. These transactions usually lack a corresponding platform transaction, and in these cases the columns for the platform are empty.

**all_platform_transactions.csv**

Contains all Open Collective platform transactions for the given host and period.

**wise_reconciliation.csv**

Contains all transactions from Wise for the given period. 
* Data from Wise is in columns prefixed "wise."
* Data from bank account transactions is in columns prefixed "bank."
* Data from the Open Collective platform is in column without a prefix.
* A reconciliation category has been included in the _reconciliation_category column.

**stripe_reconciliation.csv**

Contains all transactions from Stripe for the given period. 
* Data from Stripe is in columns prefixed "stripe."
* Data from bank account transactions is in columns prefixed "bank."
* Data from the Open Collective platform is in column without a prefix.
* A reconciliation category has been included in the _reconciliation_category column.

**paypal_reconciliation.csv**

Contains all transactions from Paypal for the given period. 
* Data from Paypal is in columns prefixed "paypal."
* Data from bank account transactions is in columns prefixed "bank."
* Data from the Open Collective platform is in column without a prefix.
* A reconciliation category has been included in the _reconciliation_category column.

**bank_reconciliation.csv**

Contains all transactions from imported bank accounts for the given period. 

* Data from bank accounts is in columns prefixed "bank."
* Data from Wise is in columns prefixed "wise."
* Data from Stripe is in columns prefixed "stripe."
* Data from Paypal is in columns prefixed "paypal."
* Data from the Open Collective platform is in column without a prefix.
* A reconciliation category has been included in the _reconciliation_category column. 
