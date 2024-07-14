# Simple Flask app which interacts with an SQLite3 database

## Installation instructions
Instructions for running the project locally: 

1. Clone repo with `git clone`
2. Instal dependencies using `pip install -r requirements.txt`

    Please note: if you get a `ModuleNotFoundError: No module named 'flask'` error, try using `pip3 install -r requirements.txt`

2. Run the Flask application using `python app.py`
3. Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/)

## Usage

![Screenshot of interface](/sqlite3-gui-screenshot.png)

**Features include:**
1. Real time data validation, as shown by the red text. This red text will appear if the user tries to submit a new record with invalid values, including the omission of a day, month, or year value.
2. Ability to update an existing record's "Name" and "Birthday" value, then subsequently using the "Save Changes" button to commit changes to the SQLite3 database. 
3. Delete existing records by clicking the "X" button. 

You may re-create the database by using the query found in `data_create.sql`.
