# Coffee Shop Management Application

A simple Python application to manage a coffee shop. This application models the basic entities of a coffee shop, such as `Coffee`, `Customer`, and `Order`, allowing you to keep track of coffees offered, customers, and their orders.

## Table of Contents
- [Coffee Shop Management Application](#coffee-shop-management-application)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Classes Overview](#classes-overview)
    - [Coffee Class](#coffee-class)
    - [Customer Class](#customer-class)
    - [Order Class](#order-class)
    - [Example of Creating an Order](#example-of-creating-an-order)
  - [Usage](#usage)
    - [Running the Application](#running-the-application)
  - [Running Tests](#running-tests)
  - [License](#license)

## Features

- **Coffee Management**: Add and manage different types of coffee, track associated orders, customers, and calculate average price.
- **Customer Management**: Add customers, retrieve their orders, and identify frequent buyers or highest spenders on specific coffees.
- **Order Management**: Place and manage orders, and keep a history of all orders with details on customers, coffees, and prices.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/silvanos-eric/coffee_shop.git
    cd coffee_shop
    ```

2. **Install dependencies using Pipenv**:

    Ensure you have [Pipenv](https://pipenv.pypa.io/en/latest/) installed, and then run:

    ```sh
    pipenv install --dev
    ```

This command will install all required packages for both development and production.

## Classes Overview

### Coffee Class

- **Purpose**: The `Coffee` class manages the details of a coffee, such as its name, related orders, and customers.
- **Important Methods**:
  - `orders()`: Returns all orders associated with this coffee.
  - `customers()`: Returns all customers who ordered this coffee.
  - `num_orders()`: Returns the number of orders placed for this coffee.
  - `average_price()`: Returns the average price of all orders for this coffee.

### Customer Class

- **Purpose**: The `Customer` class handles the customer information, such as their name, their orders, and associated coffee.
- **Important Methods**:
  - `orders()`: Returns all orders placed by the customer.
  - `coffee()`: Returns all unique coffee types ordered by this customer.
  - `create_order(coffee, price)`: Creates a new order for the customer.

### Order Class

- **Purpose**: The `Order` class represents individual orders made by customers for a specific coffee at a certain price.
- **Important Attributes and Methods**:
  - `customer`: The customer who placed the order.
  - `coffee`: The coffee ordered.
  - `price`: The price of the coffee, which must be between 1.0 and 10.0.
  - `all`: A class-level list that stores all the order instances created.

### Example of Creating an Order

```python
from Coffee import Coffee
from Customer import Customer
from Order import Order

# Create instances of Customer and Coffee
customer_1 = Customer("Alice")
coffee_1 = Coffee("Latte")

# Create an order with a valid price between 1.0 and 10.0
order_1 = Order(customer_1, coffee_1, 4.50)
```

## Usage

### Running the Application

To use this application, you can import the classes and create instances in your own scripts or an interactive Python shell:

```python
from coffee_shop import Coffee, Customer, Order

# Create a coffee
coffee = Coffee("Espresso")

# Create a customer
customer = Customer("Alice")

# Place an order
customer.place_order(coffee, 5.0)

# Check coffee statistics
print(coffee.num_orders())  # Outputs: 1
print(coffee.average_price())  # Outputs: 5.0
```

## Running Tests

Unit tests can be run using `pytest`. After setting up the project and activating the environment:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.