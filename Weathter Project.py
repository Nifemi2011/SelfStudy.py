import requests

print("\t\tWelcome to the Weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n\n")

city_name = input("Enter the name of the City: ")

def Gen_report(city):
    url = f"https://wttr.in/{city}"
    try:
        data = requests.get(url)
        report = data.text
    except:
        report = "Error Occurred"
    print(report)

Gen_report(city_name)


# When u first generate this code there could be an issue with your code either because the weather projection wasn't live so affter every line of code u refresh the page you are importing from.


# What functions we used in this code wer:
 #- Importing function - this allows us to import code from a diffrent script and use it in our current script.
#- def function -  allows to define a paricular line of code that we want to run/ generate in our code.
# - Try & except function- also like if & else statements allows us to be able to use more defined coding in our script in order to get a more deeper explanation in our line of code.
# In order to get all the weather info from the satelite copy and paste this code into your line code after url .
#   This is the code https://wttr.in/{city}
#Make sure to not forget to use ur f" this is where the link will go!"😍👍

@Nifemi_2011
@ Nifemi_2011 @vscode @github
