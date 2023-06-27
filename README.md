# Dapie

Dapie is a Docker container listing application built using PyQt5 and Docker libraries. This application displays the Docker containers on your computer to the user.

## Requirements

- Python 3.x
- PyQt5
- Docker Python module

## Installation

1. Clone the project or download it as a ZIP.

2. Open the terminal and navigate to the root directory of the project.

3. Run the following command to install the required Python packages:

   ```bash
   make
   ```

   This command executes the Makefile to install the dependencies and compile your Python script.

## Usage

1. Open the terminal and navigate to the root directory of the project.

2. Start the application by running the following command:

   ```bash
   ./dapie
   ```

3. When the application starts, a window will appear showing your Docker containers.

4. Click the "Exit" button or close the window to exit the application.

## Using Makefile

The project includes a Makefile, which automates installing the requirements and compiling your Python script.

- You can run the following command to install the requirements:

  ```bash
  make
  ```

- To create a compiled version, you can use the following command:

  ```bash
  make dapie
  ```

- You can use the following command to clean the generated files:

  ```bash
  make clean
  ```

## License

This project is licensed under the T1 License. For more information, see the [LICENSE](LICENSE) file.

## Contributing

If you would like to contribute to this project, please refer to the CONTRIBUTING file.

## Issue Reporting

If you encounter any issues, please open a GitHub issue or send me an email.