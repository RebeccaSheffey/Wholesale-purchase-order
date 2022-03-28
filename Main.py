def testNumberD():
    # note the 'D' in all the function names allows me to have variables of the same name (without the 'D')
    # tests if an input is a valid number
    while 1 == 1:   # causes input request to repeat until a valid input is given
        Input = input()
        try:
            int = (format(float(Input), '.2f'))     # tests if input can be put in ##.## format
        except:
            print("That was not a valid number. Please try again.")
        else:
            return float(Input)     # returns the value as a float
def testWordD(word1, word2):
    # tests if an input is valid (valid inputs are word1 and word2)
    while 1 == 1:   # causes input request to repeat until a valid input is given
        Input = input()
        if word1 == Input or word2 == Input:
            return Input    # returns the input
        else:
            print("That was not a valid response. Please try again.")
def checkD(n):
    # checks if the user has entered the proper input
    print("You have entered '" + str(n) + "'. Is this correct? Please enter 'yes' or 'no'")
    return testWordD("yes", "no")   # tests if the user entered yes or no
def productTitleD():
    # determines the product title
    while 1 == 1:   # causes input request to repeat until a valid input is given
        productTitle = input("Please enter a product title: ")
        test = checkD(productTitle)     # checks if the user entered the proper title
        if test == "yes":
            return productTitle
def productCostPerUnitD():
    # determines the CPU of the product
    print("Please enter the estimated cost per unit of the product: ")
    productCost = testNumberD()   # tests if the input is a valid number
    print("Please enter the estimated tax percentage(for 7%, enter '7'): ")
    tax = testNumberD() / 100   # tests if the input is a valid number and divides by 100
    tax += 1    # adds 1 to tax
    return productCost, tax     # returns both the product cost and tax
def smartPricingD():
    # determines if a user would like to enable smart pricing as described below
    print("Smart pricing will automatically decrease the cost of production based on the "
          "quantity being produced. 100+ units is 3% cheaper, 500+ is 5% and 1000+ is 10%."
          "\nWould you like to enable smart pricing? Please enter 'yes' or 'no'")
    smartPricing = testWordD("yes", "no")   # tests if the user entered yes or no
    if smartPricing == "yes":
        print("Smart pricing is now enabled.")
    return smartPricing
def productQuantityD():
    # determines the quantity of the product being bought
    print("Please enter the number of units you would like produced: ")
    productQuantity = testNumberD()   # tests if the input is a valid number
    if smartPricing == "yes":   # determines the discount given from smart pricing
        if productQuantity >= 1000:
            discount = .90
        elif productQuantity >= 500:
            discount = .95
        elif productQuantity >= 100:
            discount = .97
        else:
            discount = 1
    else:
        discount = 1
    return productQuantity, discount     # returns both the product quantity and discount
def productDescriptionD():
    # collects a product description
    productDescription = input("Please enter a product description or press enter to cancel: \n")
    if not productDescription:  # returns a null value if the user presses enter without an input
        return None
    else:
        test = checkD(productDescription)     # checks if the user entered the proper description
        if test == "yes":
            return productDescription
def calculateCostD(CPU, units, tax, smartPricing, discount):
    # calculates the total price with and without tax
    if smartPricing != "yes":
        totalPriceNoTax = CPU * units   # calculates the total price with tax
        totalPriceWithTax = totalPriceNoTax * tax   # calculates the total price without tax
    elif smartPricing == "yes":
        totalPriceNoTax = CPU * units * discount   # calculates the total price with tax
        totalPriceWithTax = totalPriceNoTax * tax   # calculates the total price without tax
    return totalPriceNoTax, totalPriceWithTax     # returns the total price with and without tax

print("Hello, welcome to this Program! It was designed to calculate the total cost of a wholesale purchase.\n"
      "You may enter multiple items into the system; however, results will only be given for one product at a time.")
print("To properly enter a product into the system, you will need a: product title, "
      "product cost, and production quantity.\nYou may choose to add a product description as well.")
# welcome messages

print("How many products would you like to enter?")
numberOfProducts = int(testNumberD())   # tests if the input is a valid number and turns it into an integer
# determines the number of products the user would like to calculate the price for

for x in range(0, numberOfProducts):
    productTitle = productTitleD()  # defines product title

    print("Would you like to enter a product description? Please enter 'yes' or 'no'")
    preference = testWordD("yes", "no")
    # determines if user would like to enter a product description

    if preference == "yes":
        productDescription = productDescriptionD()
    else:
        productDescription = None
    # defines product description

    placeHolder = productCostPerUnitD()  # placeholder for defining product CPU and tax
    productCostPerUnit = placeHolder[0]
    tax = placeHolder[1]

    smartPricing = smartPricingD()  # determines if user would like smart pricing

    placeHolder = productQuantityD()  # placeholder for defining product quantity and discount
    productQuantity = placeHolder[0]
    discount = placeHolder[1]

    placeHolder = calculateCostD(productCostPerUnit, productQuantity, tax, smartPricing, discount)
    # placeholder for defining product cost with and without tax
    totalCostNoTax = placeHolder[0]
    totalCostWithTax = placeHolder[1]

    if productDescription != None:
        print("Your project description for", productTitle, "is: ", productDescription)
        # prints the product description if there is one

    print("If you were to purchase", format(productQuantity, '.0f'), productTitle + ", it would cost $"
          + format(totalCostNoTax, '.2f'), "without tax and $" + format(totalCostWithTax, '.2f'), "with tax.\n")
    # prints the total price with and without tax
