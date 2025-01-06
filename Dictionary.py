monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}
print(monthConversions["Nov"])
print(monthConversions.get("luk","Not a valid key "))

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")