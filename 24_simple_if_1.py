#write a program to calculate & display profit/loss amount from given purchase and sales price of product. 
purchase_price = input("Enter product purchase price")
sales_price = input("Enter product's sales price")

#first convert input into integer then we can mathematical operations 
purchase_price = int(purchase_price)
sales_price = int(sales_price)

#difference 
difference = sales_price - purchase_price

if difference>0:
    print("you have made profit of ",difference)

if difference<0:
    print("you have made loss of ",difference)

print("Good bye.")
