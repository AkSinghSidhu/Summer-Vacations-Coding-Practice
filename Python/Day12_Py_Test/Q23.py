# Create a JSON file with 10 products: `{id, name, price, category, in_stock}`. Script that: loads it, filters by category, sorts by price, updates a product's price by id, adds a new product, removes a product by id, saves back. Handle file-not-found and invalid JSON as separate errors.

from pathlib import Path
import os, json, random

class ProductIdNotFound(Exception):
    pass

def loadProducts():
    try:
        with open("products.json", "r") as file:
            products = json.load(file)

    except FileNotFoundError:
        products = []

    except json.JSONDecodeError:
        products = []

    filteredCate = random.choice(products)["category"]
    print(f"Category to filter: {filteredCate}")

    filteredList = []
    for product in products:
        if product["category"] == filteredCate:
            filteredList.append(product)
            print(product)

    sortedPrices = sorted(filteredList, key = lambda x: x["price"])
    print(sortedPrices)

    updatePriceId = int(input("Enter the Product Id for changing the price: "))
    print(f"Updating the price of product with id: {updatePriceId}")
    found = False
    
    try:
        for product in products:
            if product["id"] == updatePriceId:
                updatedPrice = int(input("Enter the new Price: "))
                product["price"] = updatedPrice
                print(product)
                found = True
        
        if found == False:
            raise ProductIdNotFound
      
    except ProductIdNotFound:
        print(f"Product id: {updatePriceId} not found.")
        
    while True:
        addNewProduct = input("Want to add a new product?: ").strip().lower()
        if addNewProduct in ('true', 'yes', 'y', '1'):
            print("Enter the details of new product: ")
            proId = int(input("Enter the id of new Product: "))
            proName = input("Enter the name of the new Product: ")
            proPrice = int(input("Enter the price of new Product: "))
            proCategory = input("Enter the Category type of new Product: ")
            proStock = input("Is product in stock?: ")
            while True:
                if proStock in ('true', 'yes', 'y', '1'):
                    proStock = True
                    break
                elif proStock in ('false', 'no', 'n', '0'):
                    proStock = False
                    break
                else:
                    print("Invalid Choice")

            newProduct = {
                "id" : proId,
                "name" : proName,
                "price" : proPrice,
                "category" : proCategory,
                "in_stock" : proStock
            }
            products.append(newProduct)


        elif addNewProduct in ('false', 'no', 'n', '0'):
            break

        else:
            print("Invalid Choice")


    while True:
        remProduct = input("Want to Remove a product?: ").strip().lower()
        if remProduct in ('true', 'yes', 'y', '1'):
            remId = int(input("Enter the product id to remove the product: "))
            for product in products:
                if remId == product["id"]:
                    products.remove(product)
                    break
        
        elif remProduct in ('false', 'no', 'n', '0'):
            break

        else:
            print("Invalid Choice")


    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)


loadProducts()