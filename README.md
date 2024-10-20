# Rule Engine

## Overview
The Rule Engine is a web application that allows users to define rules using a simple input form. It parses these rules and generates an Abstract Syntax Tree (AST) for further processing. This project utilizes Flask for the backend and incorporates a user-friendly interface for easy rule creation.

## Technologies Used
- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Database**: SQLite
- **Containerization**: Docker

## Features
- User-friendly interface for entering rules
- Dynamic display of the generated AST
- Error handling for invalid rule input

## Getting Started

### Prerequisites
- **Docker**: Ensure Docker is installed on your machine. [Installation Guide](https://docs.docker.com/get-docker/)
- **Docker Compose**: This usually comes with Docker installation. If not, follow the instructions [here](https://docs.docker.com/compose/install/).

### Clone the Repository
git clone https://github.com/karanyeole/rule-engine.git
cd rule-engine

Build and Run the Application
Build the Docker containers:


docker-compose up --build
Access the application: Open your web browser and navigate to http://localhost:5000.


## Dependencies
Install the required Python dependencies by running:

pip install -r requirements.txt
Running without Docker
If you prefer to run the application locally without Docker, use the following command:

python app.py
And then navigate to http://localhost:5000.

## Design Choices
Flask: Chosen for its simplicity and flexibility, making it ideal for quick web application development.
SQLite: Used as the database for its lightweight nature and ease of setup.
Docker: Utilized for containerization, ensuring a consistent development environment across different machines.
Future Enhancements
Attribute Validation: Implement validation for rule attributes to enhance robustness.
User-Defined Functions: Allow users to define custom functions for more complex rule processing.
Contributing
Contributions are welcome! Please submit a pull request or create an issue for any suggestions or enhancements.

## License
This project is licensed under the MIT License.

