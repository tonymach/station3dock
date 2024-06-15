# Task Management Server

The Task Management Server is a Flask-based application that provides functionality for managing and tracking tasks in a research study or experiment. It allows researchers to set up sessions, receive and store task data, schedule tasks, and retrieve participant information and session statistics.

## Features

- Set up sessions for participants
- Receive and store task data during a session
- Schedule tasks based on room availability
- Retrieve participant information and session statistics
- Integration with a calendar system for scheduling and booking management
- Error handling and logging for robust operation
- Deployment-ready for local servers or cloud platforms

## Technologies Used

- Python
- Flask: A lightweight web framework for building the server application
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library for database management
- Flask-Migrate: A tool for handling database migrations
- Git: Version control system for tracking changes and collaborating with others
- GitHub: Web-based platform for hosting and managing Git repositories

## Getting Started

To get started with the Task Management Server, follow these steps:

1. Clone the repository to your local machine using the following command:
   ```
   git clone https://github.com/your-username/task-management-server.git
   ```

2. Navigate to the project directory:
   ```
   cd task-management-server
   ```

3. Create a virtual environment to isolate the project dependencies:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up the database:
   - Configure the database connection URI in the `config.py` file.
   - Run the database migrations to create the necessary tables:
     ```
     flask db upgrade
     ```

7. Start the server:
   ```
   flask run
   ```

8. Access the server in your web browser at `http://localhost:5000`.

## Contributing

Contributions to the Task Management Server are welcome! If you find any bugs, have feature requests, or want to contribute enhancements, please open an issue or submit a pull request on the GitHub repository.

When contributing, please follow the existing code style and conventions, and make sure to test your changes thoroughly.

## License

The Task Management Server is open-source software licensed under the [MIT License](LICENSE).

## Contact

If you have any questions, suggestions, or feedback, please feel free to contact the project maintainer at [email@example.com](mailto:email@example.com).

Happy task management!