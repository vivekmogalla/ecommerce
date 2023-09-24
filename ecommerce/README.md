# E-Commerce Order API

This project provides API endpoints to manage customer orders in an e-commerce system.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Requirements

- `Python 3.x`
- `Django 4.x`
- `Django Rest Framework`(optional, if using RESTful APIs)
- `db.sqlite3` (Django default database)

## Installation

### 1. Clone the repository
  - git clone https://github.com/vivek451/ecommerce.git

### 2. Install the dependencies
    cd your-project
    pip install -r requirements.txt
### 3. Configure the database settings
- Open your project/settings.py and update the database settings according to your environment.

### 4. Apply database migrations
- python manage.py migrate

## Usage
1. Start the development server
    - python manage.py runserver
2. The API endpoints will be available at [local host](http://localhost:8000/).

## API Endpoints
The following API endpoints are available:

- ###### GET /orders/{order_id}: Fetch an order by order ID.
- ###### GET /orders/average-product-count: Fetch the average number of products in all orders.
- ###### GET /orders/average-product-quantity/{product_id}: Fetch the average quantity of a single product from the orders using the product ID.


#### Django models for Product, Order and OrderProduct. These models define the Database schema of the application.
- Product model with fields: id, name, measurement
- Order model with fields: order_id, product_count
- OrderProduct model with fields: order, product, quantity

These models are the foundation for managing product orders in the application.