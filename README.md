# Mentor Mentee System

This project is a Mentor-Mentee System built using Django. This README will guide you on how to set up your development environment, including creating and activating a virtual environment with `pipenv`, and installing Django.

## Getting Started

### Prerequisites

Make sure you have the following software installed on your machine:

- Python (3.6+)
- `pip` (Python package installer)
- `pipenv` (Python packaging tool)

### Setting Up the Project

1. **Clone the repository**

   Open your terminal and clone the project repository:

   ```sh
   git clone https://github.com/ByteBender24/Mentor_mentee_system.git
   cd <your repository>
   ```

2. **Install `pipenv` if not already installed**

   If you don't have `pipenv` installed, you can install it using `pip`:

   ```sh
   pip install pipenv
   ```

3. **Create and activate a virtual environment**

   Use `pipenv` to create and activate a virtual environment:

   ```sh
   pipenv shell
   ```

   This command will create a virtual environment in the `.venv` directory and activate it. You should see your prompt change to indicate that you are now working within the virtual environment.

4. **Install dependencies**

   Install the necessary dependencies, including Django, by running:

   ```sh
   pipenv install
   ```

   This will install all the packages listed in the `Pipfile`.

5. **Run the Django development server**

   Once the dependencies are installed, you can run the Django development server:

   ```sh
   python manage.py runserver
   ```

   Open your web browser and go to `http://127.0.0.1:8000` to see your project in action.

### Managing the Virtual Environment

- **Activate the virtual environment**

  If you have already set up the virtual environment and just need to activate it, run:

  ```sh
  pipenv shell
  ```

  Open a new terminal to activate the virtual environment. (Or) once again use pipenv shell to show the path for virtual environment which is of format :
  ```C:\Users\Username\.virtualenvs\Mentor_mentee_system-Xslc23KL2```

and then use:

##### 1. Git Bash
In Git Bash, you can activate the virtual environment using the `source` command:

```sh
source /c/Users/Username/.virtualenvs/Mentor_mentee_system-Xslc23KL2/Scripts/activate
```

##### 2. Command Prompt (CMD)
In Command Prompt, you can activate the virtual environment using the `activate` script:

```cmd
C:\Users\Username\.virtualenvs\Mentor_mentee_system-Xslc23KL2\Scripts\activate.bat
```

##### 3. PowerShell
In PowerShell, you can activate the virtual environment using the `activate` script:

```powershell
C:\Users\Username\.virtualenvs\Mentor_mentee_system-Xslc23KL2\Scripts\Activate.ps1
```

- **Deactivate the virtual environment**

  To deactivate the virtual environment, simply type `exit`:

  ```sh
  exit
  ```

### Additional Commands

- **Install a new package**

  To install a new package and add it to your `Pipfile`, use:

  ```sh
  pipenv install <package-name>
  ```

- **Uninstall a package**

  To uninstall a package and remove it from your `Pipfile`, use:

  ```sh
  pipenv uninstall <package-name>
  ```

- **Run a script within the virtual environment**

  To run any script within the context of the virtual environment without activating it, use:

  ```sh
  pipenv run <command>
  ```

  For example, to run the Django development server without activating the environment:

  ```sh
  pipenv run python manage.py runserver
  ```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or feedback, please open an issue or contact the project maintainer at [harishrajselva@gmail.com].


