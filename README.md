# Food Delivery System

This repository contains a command-line food delivery application built with Python. It is designed to demonstrate Object-Oriented Programming (OOP) concepts and SOLID principles through a practical, layered architecture.

## Core Concepts & Design Patterns

The application is structured to be modular, scalable, and maintainable, employing several key design patterns:

*   **SOLID Principles**: The codebase adheres to the five SOLID principles to create a robust and flexible system.
*   **Layered Architecture**: The project is organized into distinct layers (Controllers, Services, Repositories) to separate concerns.
*   **Repository Pattern**: The `repositories` layer abstracts the data access logic. `SQLiteCustomerRepository`, `SQLiteRestaurantRepository`, and `SQLiteOrderRepository` provide concrete implementations for an SQLite database, decoupling the business logic from the data source.
*   **Strategy Pattern**: Used for handling dynamic calculations for discounts and delivery charges. Different strategies (`NoDiscount`, `PremiumDiscount`, `FestivalDiscount`, `BikeDelivery`, `CarDelivery`) can be selected at runtime without changing the context code.
*   **Factory Pattern**: The `DeliveryFactory` and `DiscountFactory` are used to create appropriate strategy objects based on user input, simplifying object creation and promoting loose coupling.
*   **Dependency Injection**: Dependencies are created in `main.py` and injected into the classes that require them (e.g., a service is initialized with a repository). This improves testability and reduces hard-coded dependencies.

## Features

*   Manage Customers:
    *   Add new customers (Normal or Premium).
    *   View a list of all existing customers.
*   Manage Restaurants:
    *   Add new restaurants.
    *   View a list of all existing restaurants.
*   Manage Orders:
    *   Create a new order for a customer from a restaurant.
    *   Apply different discount types (None, Premium, Festival).
    *   Choose different delivery methods (Bike or Car), each with its own pricing model.
    *   View a detailed list of all past orders.
*   Object Tracking:
    *   Track and display the total number of `Customer` objects created during a single run session.

## Project Structure

The project is organized into the following directories:

| Directory | Description |
| :--- | :--- |
| **`cli/`** | Contains the command-line interface logic for user interaction. |
| **`controllers/`** | Handles user input from the CLI, validates it, and calls the appropriate services. |
| **`database/`** | Manages the database connection and schema creation for SQLite. |
| **`factories/`** | Implements the Factory pattern to create instances of strategy objects. |
| **`models/`** | Defines the core data structures (`Customer`, `Restaurant`, `Order`). |
| **`repositories/`** | Implements the Repository pattern for data persistence and retrieval. |
| **`services/`**| Contains the main business logic of the application. |
| **`strategies/`**| Defines and implements various strategies for calculating discounts and delivery charges. |
| **`utils/`** | Includes helper utilities, such as input validators. |

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3

### Installation & Running

1.  Clone the repository to your local machine:
    ```sh
    git clone https://github.com/boxabhi/airtribe-python.git
    ```
2.  Navigate to the project directory:
    ```sh
    cd airtribe-python
    ```
3.  Run the application:
    ```sh
    python main.py
    ```

The application will start, and the `food_delivery.db` database file will be created automatically in the root directory if it does not exist.

### How to Use

Once the application is running, you will be presented with an interactive menu. Enter the number corresponding to the action you wish to perform.

```
Food Delivery SOLID OOP Project
1. Add Customer
2. View Customers
3. Add Restaurant
4. View Restaurants
5. Create Order
6. View Orders
7. Show Customer Object Count
8. Exit
Enter choice: