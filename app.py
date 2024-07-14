from utils.sqlite_configurations import con, cur # this configuration enables row_factory (which allows the use of dicts for SQL queries)
from utils.constant_variables import MONTHS, MONTHS_INVERSE, DAYS, YEARS
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["EXPLAIN_TEMPLATE_LOADING"] = True


################################################
#                LOAD HOME SCREEN              #
################################################
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect("/")
    else:
        # SQL query for displaying database
        directory = con.execute("SELECT * FROM directory").fetchall()
        
        # convert month digit to string
        for row in directory:
            if row["month"]:
                row["month"] = MONTHS[row["month"]]
            else:
                row["month"] = " "

        # return render_template("successful_save_alert.html")
        return render_template("index.html", directory=directory, DAYS=DAYS, MONTHS=MONTHS, YEARS=YEARS)


################################################
#                DELETE A RECORD               #
################################################
@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        id_delete = request.form.get("id")
        id_delete = int(id_delete)
        cur.execute("DELETE FROM directory WHERE id = (?)", (id_delete,))
        con.commit()

    return redirect("/")

################################################
#             EDIT & SAVE A RECORD             #
################################################
@app.route("/edit", methods=["POST"])
def edit():
    if request.method == "POST":
        # note the need to FORCE and SILENCE
        json_request = request.get_json(force=True, silent=True)

        # loop for all row values in JSONDict
        for row in json_request:
            cur.execute(
                """
                UPDATE directory 
                SET name = (?), 
                    day = (?),
                    month = (?),
                    year = (?)
                WHERE id = (?)
                """, (json_request[row]["name"], 
                     (int(json_request[row]["day"])), 
                     (MONTHS_INVERSE[json_request[row]["month"]]), #  Convert months back to digits to meet SQL data type restriction
                     (int(json_request[row]["year"])), 
                     (int(json_request[row]["id"])),)
            )

        con.commit()
        return redirect("/")

################################################
#                ADD A NEW RECORD              #
################################################
@app.route("/create_new_record", methods=["POST"])
def create_new_record():
    if request.method == "POST":
        print("success")
        # # store data in variables
        name = request.form.get("name")
        day = int(request.form.get("day"))
        month = request.form.get("month")
        year = int(request.form.get("year"))
            
        # get last id value in the db & +1 to create a unique value
        id = cur.execute("SELECT id FROM directory ORDER BY id DESC LIMIT 1").fetchone()
        id = id[0]+1
        
        cur.execute(
            """
            INSERT INTO directory (name, day, month, year, id)
            VALUES ((?), (?), (?), (?), (?))
            """, ((name), (day), MONTHS_INVERSE[month], (year), (id),)
        )
        
        con.commit()
        return redirect("/")


# uncommment for debugging mode
# if __name__ == "__main__":
#     app.run(debug=True)

app.run()