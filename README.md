# Account Book Maintaining Framework

## Overview
The Account Book Maintaining Framework is a lightweight system designed to manage and track financial transactions efficiently. It enables users to record income and expenses, categorize transactions, and generate summaries for better financial decision-making.

## Features
- Add, update, and delete transactions
- Categorize income and expenses
- Maintain daily, monthly, and yearly records
- Generate financial summaries and reports
- Data validation and error handling
- Simple and scalable architecture

## Tech Stack
- Programming Language: Python
- Libraries: Pandas, NumPy
- Storage: CSV / JSON / SQLite
- Version Control: Git

## Project Structure
account-book/
│── data/
│   └── transactions.csv
│
│── src/
│   ├── add_transaction.py
│   ├── delete_transaction.py
│   ├── update_transaction.py
│   ├── report_generator.py
│   └── utils.py
│
│── tests/
│   └── test_transactions.py
│
│── requirements.txt
│── README.md

## Installation
1. Clone the repository:
   git clone https:[//github.com/your-username/account-book.git](https://github.com/mdana5/abc)
   cd account-book

2. Install dependencies:
   pip install -r requirements.txt

## Usage
- Add a transaction:
  python src/add_transaction.py

- Update a transaction:
  python src/update_transaction.py

- Delete a transaction:
  python src/delete_transaction.py

- Generate report:
  python src/report_generator.py

## Data Format
Each transaction includes:
- Transaction ID
- Date
- Type (Income/Expense)
- Category
- Amount
- Description

Example:
ID,Date,Type,Category,Amount,Description
1,2026-03-01,Expense,Food,250,Lunch
2,2026-03-02,Income,Salary,50000,Monthly salary

## Methodology
- Input validation ensures correct transaction entries
- Data is stored in structured format (CSV/DB)
- Processing layer handles CRUD operations
- Reporting module aggregates and summarizes data

## Error Handling
- Invalid inputs are rejected with proper messages
- Duplicate transaction IDs are prevented
- Missing data fields are handled gracefully

## Future Enhancements
- GUI-based interface
- Integration with banking APIs
- Advanced analytics and visualization
- Cloud-based storage support

## Contributing
1. Fork the repository
2. Create a new branch
3. Commit changes with clear messages
4. Submit a pull request

## License
This project is licensed under the MIT License.

## Author
Developed as a financial management framework for efficient bookkeeping and transaction tracking.
