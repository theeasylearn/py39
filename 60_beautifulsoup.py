html = """<!DOCTYPE html>
<html>
<head>
    <title>My Store</title>
</head>
<body>

    <h1>My Products</h1>
    <p>our all products are listed below</p>
    <span>bhavnagar</span>
    <div class="product">
        <h2>Laptop</h2>
        <p class="price">₹55,000</p>
        <p class="category">Electronics</p>
    </div>

    <div class="product">
        <h2>Mobile Phone</h2>
        <p class="price">₹25,000</p>
        <p class="category">Electronics</p>
    </div>

    <div class="product">
        <h2>Headphones</h2>
        <p class="price">₹2,500</p>
        <p class="category">Accessories</p>
    </div>
    <footer>THE EASYLEARN ACADEMY</footer>
</body>
</html>"""
# import BeautifulSoup
from bs4 import BeautifulSoup

# Create BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Get page title
print(soup.title.text)

# Get main heading
print(soup.h1.text)

#get text in footer 
print(soup.footer.text)

print(soup.p.text)
print(soup.span.text)

#return list of all div tags which has class product
products = soup.find_all("div", class_="product")

for product in products:
    price = product.find("p", class_="price").text
    category = product.find("p",class_="category").text
    print(product.h2.text,price,category)