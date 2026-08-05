# concept of arbitrary(argument are not fixed it can be range from 1 to N) argument function in python 
#count all the countries in asia 
def getAsianCountryCount(*countries):
    asian_countries = [
    "Afghanistan",
    "Armenia",
    "Azerbaijan",
    "Bahrain",
    "Bangladesh",
    "Bhutan",
    "Brunei",
    "Cambodia",
    "China",
    "Cyprus",
    "Georgia",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Israel",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Lebanon",
    "Malaysia",
    "Maldives",
    "Mongolia",
    "Myanmar",
    "Nepal",
    "North Korea",
    "Oman",
    "Pakistan",
    "Palestine",
    "Philippines",
    "Qatar",
    "Saudi Arabia",
    "Singapore",
    "South Korea",
    "Sri Lanka",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Thailand",
    "Timor-Leste",
    "Turkey",
    "Turkmenistan",
    "United Arab Emirates",
    "Uzbekistan",
    "Vietnam",
    "Yemen"
    ]
    count = 0
    for item in countries:
        if item in asian_countries:
            count = count + 1
    return count


count = getAsianCountryCount("India","China","Japan","Germany","France","United Kingdom","Italy","Canada","United States","Mexico","Brazil","Argentina","Chile","South Africa","Nigeria","Egypt","Australia","New Zealand","Fiji","Papua New Guinea","Vietnam")
print("asia country count = ",count)