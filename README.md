# Centime_Playwright_Automation
This repository contains an end-to-end test automation framework built using Playwright, Pytest, and Python for Swag lab website(https://www.saucedemo.com/)

### POM explanation
- PlaywrightTests: contains actual tests like test_login.py
- PageObject:  Page Object Models for all pages: login_page.py
- Utils:  Utilities & helpers: config.py, excel_reader.py # to read data from excel file
- TestData: TestData.xlsx 
- conftest.py: global fixtures
- Reports: report is present and trace 
- requirements.txt: Project dependencies

### Setup steps
- Clone the repository from Git: git clone "repo_url" 
- Open the project in pycharm/vs code 
- create virtual environment: python -m venv venv
- Activate the virtual environment: venv\Scripts\activate
- Run requirements.txt file : pip install -r requirements.txt 
- Install Playwright browsers : playwright install

### Test execution commands
- Run a specific test file : pytest PlaywrightTests/ 
- Run all tests : pytest Run on specific browser : pytest --browser (Supported: chromium, firefox, webkit) 
- Run with tracing options: pytest --browser --tracing (supported: on, off, retain-on-failure) 
- Run tests in parallel : pytest -n

### To see the traces
- playwright show-trace Reports/trace.zip

### Report generation
- pytest --html=report.html
- with all arguments and 1 worker: pytest --browser chromium --tracing on --html=NormalReports/report.html
- with all arguments and 3 worker pytest -n 3 --browser chromium --html=ParallelRunReport/report.html
