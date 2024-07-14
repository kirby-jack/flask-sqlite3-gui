from datetime import datetime

################################################
#                CONSTANT VARIABLES            #
################################################
MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
MONTHS_INVERSE = {value: key for key, value in MONTHS.items()}
DAYS = [i for i in range(1, 32)]
YEARS = [i for i in range(1900, datetime.now().year)]