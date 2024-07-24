function validate(form) {

    // define local variables from 'new contact' form
    const input_name = form.querySelector("input[name=name]")
    const name = input_name.value.toString().trim() // trim() removes leading & trailing white spaces
    const name_error = document.querySelectorAll('div[name="add_new_user_name_error"].error')
    
    const select_day = form.querySelector("select[name=day]")
    const day = form.querySelector("select[name=day]").value
    const day_error = document.querySelector('div[name="add_new_user_day_error"].error')
    
    const select_month = form.querySelector("select[name=month]")
    const month = form.querySelector("select[name=month]").value
    const month_error = document.querySelector('div[name="add_new_user_month_error"].error')
    
    const select_year = form.querySelector("select[name=year]")
    const year = form.querySelector("select[name=year]").value
    const year_error = document.querySelector('div[name="add_new_user_year_error"].error')
    
    // define validation check matrix
    var validation_matrix = {
        name_valid: false,
        day_valid: false, 
        month_valid: false, 
        year_valid: false
    }

    ////////////////////////////////////////////////////////
    //         VALIDATION & DISPLAY ERROR MESSAGES        //
    ////////////////////////////////////////////////////////

    // validate name - regex allows case-insensitive (/i), alphabet, spaces, and hyphens
    const regex_validate_name = /^([(a-z)(\-)\s]+)$/i;
    if ((!regex_validate_name.test(name)) && (name.toString().length < 255)) {
        name_error.forEach(element => element.style.visibility = 'visible')
        
        input_name.addEventListener("input", () => {
            name_error.forEach(element => element.style.visibility = 'hidden')
        });
    }
    else {
        validation_matrix["name_valid"] = true
    };

    // validate day - (html default value is empty string " ")
    if (!day) {
        day_error.style.visibility = 'visible';
        select_day.addEventListener("input", () => {
            day_error.style.visibility = 'hidden'
        })
    }
    else {
        input_name.value = name // this inputs the trimmed string value
        validation_matrix["day_valid"] = true
    }

    // validate month
    if (!month) {
        month_error.style.visibility = 'visible';
        select_month.addEventListener("input", () => {
            month_error.style.visibility = 'hidden'
        })
    }
    else {
        validation_matrix["month_valid"] = true
    }

    // validate year
    if (!year) {
        year_error.style.visibility = 'visible';
        select_year.addEventListener("input", () => {
            year_error.style.visibility = 'hidden'
        })
    }
    else {
        validation_matrix["year_valid"] = true
    }

    ////////////////////////////////////////////////////////
    //               SUBMIT FORM IF VALID                 //
    ////////////////////////////////////////////////////////
    if (Object.values(validation_matrix).every(Boolean)) { // converts the object to an array and checks if every value is true
        form.submit();
    }

}
