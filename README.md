# FastAPI CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built with FastAPI and Pydantic. The application provides an API for managing a list of products.

## Features

- **Get products**: The `GET /products` route returns a list of all products.
- **Get a specific product**: The `GET /products/{product_id}` route returns the product with the provided ID.
- **Create a product**: The `POST /products` route creates a new product and adds it to the list of products. Input data validation is performed automatically thanks to Pydantic, and additional validation is provided by a custom validator in the `Product` model to ensure that the price and stock are positive numbers.
- **Update a product**: The `PUT /products/{product_id}` route updates the product with the provided ID.
- **Delete a product**: The `DELETE /products/{product_id}` route deletes the product with the provided ID.

The `Product` model uses Pydantic's `validator` decorator to add a custom validation rule. This rule checks that the `price` and `stock` fields are positive numbers, and raises a `ValueError` if they are not. This ensures that it's not possible to create or update a product with a negative price or stock.


## Technologies Used

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Pydantic**: A data parsing library for Python that provides data validation through Python type annotations.

## How to Run the Project

1. Clone this repository.
2. Install the project dependencies. If you're using [Poetry](https://python-poetry.org/), you can do this with `poetry install`.
3. Run the project with `poetry run start`.

The application will run on `localhost:5000`.


## OpenAPI and Interactive API documentation

FastAPI automatically generates an OpenAPI schema for your API. This schema is available at the `/openapi.json` endpoint of your application. For example, if your application is running on `localhost:5000`, you can access the OpenAPI schema at `http://localhost:5000/openapi.json`. The OpenAPI schema is a machine-readable description of your API which can be used by various tools for documentation, code generation, or to facilitate client-side API integration.

In addition to the OpenAPI schema, FastAPI also provides an interactive API documentation using Swagger UI. This is available at the `/docs` endpoint of your application, for example, `http://localhost:5000/docs`. This interactive documentation allows you to explore your API, see the expected request structure, make test requests, and view the responses, all from your browser.

## Contributing

Contributions are welcome! Please open an issue if you find a bug, or a pull request if you have a feature or fix to contribute.
