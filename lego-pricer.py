# Grant Zukowski
# Lego Lot Pricer
# Last update 3/7/2015

# This program is designed to take up to 20 inputs with two values
# set number and set condition
# and return the price according to the website bricklinks.com.

# import urllib.request
import urllib.request

# main
def main():

    answer = input('Would you like to check lego prices? ')

    price_list = []
    while answer:
        if answer.lower() == 'y':
            price_list.append(find_price())
        elif answer.lower() == 'n':
            break
        answer = input('Would you like to check lego prices? ')

    print (sum(price_list))
    
        
    
    #ask the user how many lots they want to enter
    #lots = input(int('Number of sets in lot: '))

    # ask user for input

    
#put the set numbers into a list
#put the condition input into a list
#create an empty list to add prices to

#For each input
    #put input into a url string
    #search html from url string for data matching a price
    #add price to list
#Add up all the values in the list
#format and print the values

def find_price():

    # gather input
    setNum = input("What is the set number: ")
    if len(setNum) < 5:
        setNum += '-1'

    condition = input("What is the condition: ")

    urlrequest = 'http://www.bricklink.com/catalogPG.asp?S=' + setNum
    
    response = urllib.request.urlopen(urlrequest)

    html = response.read()

    html = str(html)
    
    price = []
    
    individual_price = []

    counter = 0
    for i in range(0, len(html) - 40):
        if html[i] == '$':
            price.append(html[i:i+10])

    if condition == 'N':
        c = 1
    elif condition == 'U':
        c = 5
    
    for i in price[c]:
        if i.isnumeric():
            individual_price.append(str(i))
          
    individual_price.insert(-2,'.')
    return (float(''.join(individual_price)))


# call main
main()

