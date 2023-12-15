# Airbnb Clone Project(the console)

This project is an Airbnb clone developed in Python, focusing on building a command-line interpreter to manage various objects within the application.

## Project Overview

The project's main goal is to create a simplified version of Airbnb's functionality. It includes the implementation of a command-line interpreter designed to manage different objects within the application. The key aspects of the command interpreter include:

### Command Interpreter Description

The command-line interpreter facilitates the following functionalities:

- **Object Creation:** Allows the creation of new objects (e.g., User, State, City, Place).
- **Object Retrieval:** Retrieves objects from files or databases.
- **Operations on Objects:** Provides capabilities like counting, computing statistics, etc.
- **Updating Attributes:** Enables the modification of object attributes.
- **Object Deletion:** Allows for the deletion of objects.

### Getting Started

To start the command-line interpreter:

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the command interpreter by executing `./console.py` in the terminal.

### Usage

Once the command interpreter is started, the following commands can be used:

- `create <classname>`: Create a new instance of a class.
- `show <classname> <id>`: Show the details of a specific instance.
- `destroy <classname> <id>`: Destroy a specific instance.
- `update <classname> <id> <attribute> <value>`: Update attributes of a specific instance.
- `all <classname>`: Display all instances of a class or a specific instance.

### Examples

Here are some examples of using the command-line interpreter:

- Creating a new User: `create User`
- Showing details of a specific Place: `show Place 123`
- Updating the name attribute of a City: `update City 456 name "New City"`

## Author

- **Rodgers Kamota**
  - GitHub: [uncorrectedlie364](https://github.com/uncorrectedlie364)
  - Email: mcclarerodgy@gmail.com

## Acknowledgments

- This project is part of a series focusing on building a full web application inspired by Airbnb.
- Special thanks to:
