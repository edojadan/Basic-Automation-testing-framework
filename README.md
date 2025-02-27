# Basic Automation Testing Framework

## Overview
This is a basic automation testing framework built using **Selenium and Python** with **pytest** as the test runner. The framework follows the **Page Object Model (POM)** to ensure maintainability and scalability. It supports **automated UI testing** for web applications, making it a useful tool for ensuring the stability of web interfaces.

## Features
- **Automated Browser Testing** using Selenium WebDriver.
- **Page Object Model (POM) Implementation** for easy maintainability.
- **Test Execution with pytest**, including **HTML Reports**.
- **Configurable Test Settings** in `config.py`.
- **Logging Mechanism** for debugging test failures.

## What I Enjoyed the Most
One of the most enjoyable aspects of building this project was designing the **test automation for login and search functionality**. where ensuring system stability and efficiency is a key responsibility. Debugging test cases and making sure elements were correctly located and interacted with gave me alot of insights into real-world automation challenges.

## How I Built This - Step-by-Step

### **1. Setting Up the Environment**
- Created a virtual environment using:
  ```sh
  python -m venv venv
  source venv/bin/activate  # Mac/Linux
  venv\Scripts\activate  # Windows
  ```
- Installed necessary dependencies:
  ```sh
  pip install -r requirements.txt
  ```

### **2. Structuring the Framework**
I followed a structured approach to make the framework modular:
- **`pages/`**: Contains page objects for different sections of the website.
- **`tests/`**: Stores test cases written using pytest.
- **`utils/`**: Contains helper functions such as logging and configuration settings.

### **3. Implementing the Base Page Class**
- Created a `BasePage` class to handle common web interactions like locating elements.
- Used **WebDriverWait** for better element handling.

### **4. Developing the Login and Search Pages**
- Implemented `LoginPage` with methods for entering credentials and submitting the login form.
- Built `SearchPage` to input queries and verify search results.

### **5. Writing Test Cases**
- Created `test_login.py` to verify login functionality.
- Developed `test_search.py` to ensure the search feature works correctly.
- Used **pytest assertions** to validate test success.

### **6. Adding Test Execution Configuration**
- Implemented **pytest fixtures** in `conftest.py` to handle browser setup and teardown.
- Configured `pytest.ini` to define test paths and reporting settings.

### **7. Running the Tests and Generating Reports**
To execute tests and generate an HTML report, I used:
```sh
pytest --html=report.html --self-contained-html
```

### **8. Debugging and Enhancements**
- Added logging to track errors.
- Used `webdriver-manager` to automate driver management.
- Improved test stability by handling dynamic elements using **explicit waits**.

## How to Run the Tests
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/edojadan/Basic-Automation-testing-framework.git
   cd Basic-Automation-testing-framework
   ```

2. **Set Up Virtual Environment** (Optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Run Tests**:
   ```sh
   pytest --html=report.html --self-contained-html
   ```

5. **View Test Report**:
   ```sh
   open report.html  # Mac/Linux
   start report.html  # Windows
   ```

## Future Enhancements i might add
- **Expand test coverage** for additional functionalities.
- **Integrate CI/CD** to automate test execution.
- **Add parallel test execution** for efficiency.

I want this project to provide a solid foundation for **web automation testing**. It was an exciting and insightful project to build!


