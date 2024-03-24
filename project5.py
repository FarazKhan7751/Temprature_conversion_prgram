import requests
from bs4 import BeautifulSoup
import csv

def extract_product_info(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find product information
    products = soup.find_all('div', class_='product')  # Assuming products are wrapped in <div class="product">

    product_data = []
    for product in products:
        name = product.find('h2', class_='product-name').text.strip()
        price = product.find('span', class_='product-price').text.strip()
        rating = product.find('span', class_='product-rating').text.strip()

        # Append data to the list
        product_data.append((name, price, rating))

    return product_data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Price', 'Rating'])
        writer.writerows(data)

if __name__ == "__main__":
    # URL of the e-commerce website
    url = 'https://www.daraz.pk/'  # Replace with actual URL

    # Extract product information
    product_info = extract_product_info(url)

    # Save data to CSV file
    save_to_csv(product_info, 'product_info.csv')

    print("Product information has been extracted and saved to product_info.csv")
