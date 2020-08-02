#importing flask
from flask import Flask 
import datetime

#flask constructor 
app = Flask (__name__, static_url_path="/static")

@app.route('/lab7')
def coffeeIndex():
    myReply = coffeeTitle()
    myReply += coffeeTime()
    myReply += coffeeBody()
    myReply += coffeeTable()
    myReply += coffeeLogin()
    myReply += coffeeEnd()

    return myReply
    
def coffeeTitle():
     titleData = "<!--My webpages title--->"
     titleData += " <!DOCTYPE html> "
     titleData += " <html> "
     titleData += " <!---My title----> "
     titleData += " <head> "
     titleData += "<title> My Coffee Shop </title>"
     titleData += "<br></br>"
     titleData += "<img  height='200px' width='200px' src=' /static/iced-latte-at-coffee-shop-window.jpg' alt='icecoffeeandshoppingwindow'>"
     titleData += "<br></br>"
     titleData += " </head> "
     return titleData

def coffeeBody():
    bodyData = "<body>"
    bodyData += "<!-- Welcome to page-->"
    bodyData += "<h1> Welcome to my Coffee Shops Website </h1>"
    bodyData += "<br></br>"
    
    
    bodyData += "<!-- Image---->"
    bodyData += "<img height='200px' width='200px' src= '/static/journal-and-coffee-at-table.jpg' alt='coffeeandJournal'>"
    bodyData += "<br></br>"
    bodyData += "<!-- Image---->"
    bodyData += "<img height='200px' width='200px' src= '/static/barista-pours-over-coffee-at-cafe.jpg' alt='baristaphoto'>"
    bodyData += "<br></br>"
    
    bodyData += "<!--Coffee Menu title and ordered list-->"
    bodyData += "<h2>  Menu of Coffee Drinks </h2>"
    bodyData += "<!-- Ordered list of Coffee Menu--->"
    bodyData += "<br></br>"
    bodyData += "<ol>"
    bodyData += "<li> Drip Coffee </li>"
    bodyData += "<li> Espresso </li>"
    bodyData += "<li> Cold Brew </li>"
    bodyData += "<li> Red Eye </li>"
    bodyData += "<li> Americano </li>"
    bodyData += "<li> Latte </li>"
    bodyData += "</ol>"
    bodyData += "<br></br>"
    bodyData += "<!-- Image---->"
    bodyData += "<img height='200px' width='200px' src= ' /static/self-serve-coffee-shop.jpg'>"
    bodyData += "<br></br>"
    
    bodyData += "<!-- Unordered list of food items the coffee shop sells--> "
    bodyData += "<h3> Menu of Food Items </h3>"
    bodyData += "<ul>"
    bodyData += "<li> Donuts </li>"
    bodyData += "<li> Scones </li>"
    bodyData += "<li> Muffins </li>"
    bodyData += "<li> Bagles </li>"
    bodyData += "<li> Egg Bites </li>"
    bodyData += "</ul>"
    bodyData += "<br></br>"
    
    bodyData += "<!-- Links--->"
    bodyData += "<ul>"
    bodyData += "<h3> Our Favorite Coffee Blogs </h3>"
    bodyData += "<li><a href= 'http://dailycoffeenews.com/html/'> 1. Daily Coffee News </a></li>"
    bodyData += "<li><a href= 'http://sprudge.com/html/'> 2. Sprudge </a></li>"
    bodyData += "<li><a href= 'https://starbucks.com/html/'> 3. Starbucks </a></li>"
    bodyData += "</ul>"
    bodyData += "<br></br>"
    return bodyData
 
def coffeeTable():
    tableData = "<!--This is the data table -->"
    tableData += "<table border=1>"
    tableData += "<caption> World Coffee Conumption </caption>"
    tableData += "<tr>"
    tableData += "<th>Countries</th>"
    tableData += "<td>Africa</td>"
    tableData += "<td>Asia</td>"
    tableData += "<td>Europe</td>"
    tableData += "<td> USA </td>"
    tableData += "</tr>"
    
    tableData += "<tr>"
    tableData += "<th>2016</th>"
    tableData += "<td>11130</td>"
    tableData += "<td>34573</td>"
    tableData += "<td>52045</td>"
    tableData += "<td>29559</td>"
    tableData += "</tr>"
    
    tableData += "<tr>"
    tableData += "<th>2017</th>"
    tableData += "<td>11527</td>"
    tableData += "<td>35697</td>"
    tableData += "<td>53148</td>"
    tableData += "<td>3900</td>"
    tableData += "</tr>"
    
    tableData += "<tr>"
    tableData += "<th>2018</th>"
    tableData += "<td>11939</td>"
    tableData += "<td>36470</td>"
    tableData += "<td>55731</td>"
    tableData += "<td>31876</td>"
    tableData += "<br></br>"
    tableData += "</tr></table>"
    
    return tableData

def coffeeLogin():
    loginData = "<h1> Coffee Shop Rewards Login </h1>"
    loginData += "<h2> Please Log In </h2>"
    
    loginData +="<form action='/form-processing-script' method='post'>"
    
    loginData += "<!--Username label and input-->"
    loginData += "<label for='username'>Username</label><input type='text' name='username'>"
    
    loginData += "<!--Password label and input-->"
    loginData += "<label for='password'Password</label> <input type='password' name='password'> "
    
    loginData += "<!--Submit and Reset buttons-->"
    loginData += "<input type='submit' value='Send Form Data'>"
    loginData += "<input type='reset' value= 'Clear Form'>"
    
    loginData += "<br></br>"
    loginData += "<!--Drop Down menu-->"
    loginData += "<label for= 'decision'> Would you like to be added to our email list?</label>"
    loginData += "<select id='decision'>"
    loginData += "<option> Yes </option>"
    loginData += "<option> No </option>"
    loginData += "</select>"
    loginData += "<br></br>"
    loginData += "</form>"
    
    return loginData

def coffeeTime():
    timeData = "<!--Uses python datetime to display todays time and date -->"
    timeData += "<!--Todays date--->"
    timeData += "<!-- displays time & date-->"
    timeData += "Todays date and time is :" + str(
        datetime.datetime.now().ctime())
    return str(timeData)


def coffeeEnd():
     endPage = "</body>"
     endPage += "</html>"
     return endPage
     
app.run(host='0.0.0.0', port = 8080)