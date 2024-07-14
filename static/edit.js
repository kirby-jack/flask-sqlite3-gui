function saveChanges() {

    const rowCount = document.querySelectorAll("div[name='data'] table tbody tr").length // total number of tr elements (rows)
    const columnCount = document.querySelectorAll("div[name='data'] table tbody tr")[0].querySelectorAll("td").length // total number of td elements (columns) per row 

    const JSONDict = {} // this will store data, be converted to JSON and passed to flask

    // for each row
    for (let i = 0; i < rowCount; i++) {

        let name, day, month, year, id; // declare variable
        let row_data = document.querySelector(`tbody tr:nth-child(${i + 1})`).querySelectorAll("td"); // select all table rows by ID (ID matches SQL ID)
        
        // collect id value
        id = row_data[1].getAttribute("id")
        
        // for each column
        for (let j = 0; j < columnCount - 1; j++) {
            var columnName = row_data[j].getAttribute('name') // get column name

            // collect values for all columns per row 
            if (columnName == 'NameCol') {
                name = row_data[j].innerHTML
                // if (!validateString(name)) 
            } else if (columnName == 'BirthdayCol') {
                day = row_data[j].querySelectorAll("select")[0].value
                month = row_data[j].querySelectorAll("select")[1].value
                year = row_data[j].querySelectorAll("select")[2].value
            }
        }
    
        // store in dict which will be converted to JSON
        JSONDict[i] = {
            name: name,
            day: day, 
            month: month, 
            year: year,
            id: id
        }
    }

    // Send JSON dict to flask 
    const fetchPromise = fetch("/edit", {
        method: "POST",
        body: JSON.stringify(JSONDict)
    });
    fetchPromise
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error: ${response.status}`);
            }
            else {
                alert("Save successful!")
                window.location.href = '/';
            }

        })
}