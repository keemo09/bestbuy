# Store Application

This is a simple store application written in Python. The application allows you to manage a list of products, make orders, and handle promotions for different products.

## Features

- View all available products.
- Check the total quantity of products in stock.
- Make an order by selecting a product and its quantity.
- Manage promotions for different products.
- Calculate total price after applying promotions.

## API Endpoints

### **`GET /`**: Fetch all products in store
- **Response**: A JSON array containing product details.
  - Example:
    ```json
    [
        {"name": "MacBook Air M2", "price": 1450, "quantity": 100},
        {"name": "Bose QuietComfort Earbuds", "price": 250, "quantity": 500}
    ]
    ```

### **`GET /total`**: Fetch the total quantity of products in store
- **Response**: The total quantity of all products in the store.
  - Example:
    ```json
    1450
    ```

### **`POST /order`**: Create a new order
- **Request Body**: A JSON array containing product IDs and quantities.
  - Example:
    ```json
    [
        {"product_id": 1, "quantity": 2},
        {"product_id": 3, "quantity": 1}
    ]
    ```
- **Response**: The total price after applying any promotions.
  - Example:
    ```json
    {"message": "Order successful", "total": 3000.50}
    ```

## Product Management

Products can have different types:

- **Standard Products**: Regular products with stock and price.
- **Non-Stocked Products**: Products that are not limited by quantity.
- **Limited Products**: Products with a maximum quantity limit.

## Promotions

The store supports various types of promotions:

- **Second Half Price**: 50% discount after the first half of the order.
- **Third One Free**: Get one free product for every three products purchased.
- **Percent Discount**: Apply a percentage discount to the product price.



## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md).



## Contact

Created by [keemo09](https://github.com/keemo09) - feel free to reach out!
