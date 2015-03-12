# Grant Zukowski
# Lego Lot Pricer
# Last update 3/11/2015

# This program is designed to take up to 20 inputs with two values
# set number and set condition
# and return the price according to the website bricklinks.com.

# import urllib.request
import urllib.request

# main
def main():

    # open the text file with all of the set numbers
    f_input = open('Book1.txt', 'r')

    # create a variable that is the first line of the file
    line = f_input.readline()

    # strip off the newline character at the end of it
    clean_line = line.rstrip('\n')

    # create a container list that all the prices can be added to    
    price_list = []

    # while there is a line to read, find its price and add the price to
    # the list, then try to read the next line
    while line:
        clean_line = line.rstrip('\n')
        price_list.append(find_price(clean_line))

        line = f_input.readline()
    
    # once all the lines have been read, add them up and print them.
    print (sum(price_list))
    

def find_price(clean_line):

    # set the input variable and add '-1' if the number is to short
    setNum = clean_line
    if len(setNum) < 6:
        setNum += '-1'

    # create a variable with the url and set number combined
    urlrequest = 'http://www.bricklink.com/catalogPG.asp?S=' + setNum

    # use the variable to make a request to the URL
    response = urllib.request.urlopen(urlrequest)

    # create a variable and read all the html data in
    html = response.read()

    # convert the html data into a string
    html = str(html)

    # create a place to store all of the prices
    price = []

    # create a place to store the individual price you want
    individual_price = []

    # go through the entire html string and find any dollar sign, when you do
    # take the 10 characters after the dollar sign and add them to price
    for i in range(0, len(html) - 40):
        if html[i] == '$':
            price.append(html[i:i+10])

    # variable for new or used price.  New is c = 1, used is c = 5
    c = 5

    # go through all the characters of the string of the price you want and
    # add anything that is a number to the price list
    for i in price[c]:
        if i.isnumeric():
            individual_price.append(str(i))

    # add a decimal point to the price list      
    individual_price.insert(-2,'.')

    # join the entire price list together, convert it to a float, and return it
    return (float(''.join(individual_price)))


# call main
main()
