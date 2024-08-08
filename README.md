# Python Code Executor API

This project is a simple Django-based web application that allows users to execute Python code securely within an isolated Docker container. It provides an API endpoint where users can send Python code via a POST request, and the application will execute the code and return the result.

## Features

- **Secure Code Execution**: Python code is executed inside an isolated Docker container, preventing it from affecting the host system.
- **Resource Limiting**: Each container is limited in memory (500 MB) and CPU (2 CPUs) to prevent excessive resource usage.
- **Timeout Handling**: Code execution is capped at 30 seconds to avoid long-running or infinite loops.

## Endpoints

### `POST /run_code`

Executes the provided Python code in a Docker container and returns the output or any errors.

#### Request

- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body**:
  ```json
  {
    "code": "your_python_code_here"
  }

#### Resopnse

- **Status**: `200 OK`
- **Body**:
  ```json
  {
    "output": "result_of_code_execution",
    "error": ""
    }

#### Error

- **Status**: Varies based on the error
- **Body**:
    ```json
    {
    "error": "description_of_error"
    }

#### Possible Errors

- **400 Bad Request**: No code provided in the request body.
- **405 Method Not Allowed**: Request method is not `POST`.
- **500 Internal Server Error**: An error occurred during code execution, such as a timeout or execution failure.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/thiSSSnake/intepreter.git
   cd interpreter

2. **Install dependencies**:
    ```bash
    pip instal -r requirements.txt

3. **Ensure Docker is installed and running.**

4. **Run the application**:
    ```bash
    python manage.py runserver

## Security Considerations

- **The code execution environment is isolated in a Docker container to prevent it from accessing or modifying the host system.**

- **Resource limits (memory and CPU) are enforced to protect against resource exhaustion attacks.**

- **Code execution is limited to 30 seconds to prevent infinite loops or excessively long-running scripts.**