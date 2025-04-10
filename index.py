# to calculayte age of a person
import datetime
from datetime import date
def agecal(birth):
    # birth=date("enter birth date yyyyy-mm-d")
    today=date.today()
    yearage=today.year-birth.year-1
    monthage=today.month+12-birth.month
    dayage=abs(today.day-birth.day)
    print(f"{yearage} years {monthage} months {dayage} days")
   
    
agecal(date(2000,6,15)) 
# agecal()
