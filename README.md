# Coffee Shop Management System

A Python-based application for managing coffee shop operations, including customer management, order processing, and coffee inventory management.

## Table of Contents

- [Coffee Shop Management System](#coffee-shop-management-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Tests](#running-tests)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- Manage coffee inventory and details.
- Handle customer information and orders.
- Process and track customer orders.
- Comprehensive test coverage for core functionalities.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone git@github.com:silvanos-eric/coffee_shop.git
    cd coffee_shop
    ```

2. **Install dependencies:**

    Make sure you have [Python](https://www.python.org/downloads/) installed. Use [Pipenv](https://pipenv.pypa.io/en/latest/) to install dependencies:

    ```sh
    pipenv install
    ```

## Usage

To use the Coffee Shop Management System, you can run the main scripts in the `src/coffee_shop/` directory.

For example, to manage coffee inventory:

```sh
python src/coffee_shop/coffee.py
```

To manage customer data:

```sh
python src/coffee_shop/customer.py
```

To process orders:

```sh
python src/coffee_shop/order.py
```

## Running Tests

To run the test suite, use the following command:

```sh
pipenv run pytest
```

This will execute all tests located in the `tests/` directory.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add your feature'`).
5. Push to the branch (`git push origin feature/YourFeature`).
6. Open a Pull Request.

## License

This project is licensed under the terms of the [MIT License](LICENSE.md).