# Order Management System

This project implements a simple order management system using hexagonal architecture in Python. The application allows for the creation, processing, and listing of orders.

## Project Structure

The project is divided into the following main modules:

- `domain/`: Contains the business entities.
- `ports/`: Defines the interfaces (ports) for communication between the business logic and adapters.
- `adapters/`: Implements adapters for data persistence (in-memory repository).
- `services/`: Contains application logic (services).
- `main.py`: The entry point of the application.

## How to Run

To run the system, follow these steps:

1. Clone the repository to your local machine.
2. Ensure Python is installed.
3. Navigate to the project folder and run the `main.py` file:

   ```bash
   python main.py
