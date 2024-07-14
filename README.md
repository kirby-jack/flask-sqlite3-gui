# Simple Flask app which interacts with an SQLite3 database

## Installation instructions
Instructions for running the project locally: 

1. Instal dependencies using `pip install -r requirements.txt`

    Please note: if you get a `ModuleNotFoundError: No module named 'flask'` error, try using `pip3 install -r requirements.txt`

2. Run the Flask application using `python app.py`
3. Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/)

## Usage

![Screenshot of interface](/sqlite3-gui-screenshot.png).

**Features include:**
1. Real time data validation. The user will not be able to submit a new record unless values are correctly entered.
2. Updating an existing record's "Name" and "Birthday" values, then use the "Save Changes" button to commit changes to the database. 
3. Delete existing records by clicking the "X" button. 

You may re-create the database by using the query found in `data_create.sql`.