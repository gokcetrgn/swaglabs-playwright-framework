# SwagLabs Playwright Automation

A UI test automation framework for the Swag Labs demo application, developed during my internship at **Kafein Technology**.

## Tech Stack

- Python
- Playwright
- Pytest
- Allure Report

## Project Structure

```
├── common/
├── data/
├── projects/
│   └── Swaglabs/
│       ├── pages/
│       ├── cases/
│       └── scenarios/
├── results/
└── conftest.py
```

## Features

- Login tests
- Product navigation
- Add/Remove cart items
- Product sorting
- Cart tests
- Checkout tests
- Overview & Complete order tests
- Allure reporting
- Video recording on test failure

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Run Tests

```bash
pytest
```

## Generate Allure Report

```bash
allure serve results/allure-results
```

## Notes

This project was developed for learning and internship purposes using the Swag Labs demo application.
