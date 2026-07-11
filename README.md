# Swag Labs Test Automation Framework

A UI test automation framework for the Swag Labs demo application, developed during my internship at Kafein Technology.

## Tech Stack

- Python
- Playwright
- Pytest
- Allure Report
- Pytest-xdist
- GitHub Actions
- JSON (Data-Driven Testing)
- YAML Configuration

---

## Project Structure

```
├── common/
├── data/
│   ├── SwagLabs/
├── projects/
│   └── Swaglabs/
│       ├── pages/
│       ├── cases/
│       └── scenarios/
├── results/
├── .github/
│   └── workflows/
├── conftest.py
├── main.py
└── requirements.txt
```

---

## Features

- UI Test Automation with Playwright
- Page Object Model (POM)
- Step Layer Architecture
- Data-Driven Testing using JSON
- Multi-browser execution (Chromium & Firefox)
- Parallel test execution with Pytest-xdist
- Allure Report integration
- Automatic video recording on failed tests
- GitHub Actions CI integration

### Test Coverage

- Login Tests
- Product Navigation
- Product Sorting
- Add / Remove Cart Items
- Cart Tests
- Checkout Tests
- Overview & Complete Order Tests

---

## Performance

Parallel execution is supported using **pytest-xdist**.

| Execution Mode | Duration |
|---------------|---------:|
| Sequential | **1 min 52 sec** |
| 4 Workers | **1 min 00 sec** |

✅ Test execution time was reduced by approximately **46%** using 4 parallel workers.

---

## Installation

```bash
pip install -r requirements.txt
playwright install
```

---

## Run Tests

```bash
python main.py
```

or

```bash
pytest
```

---

## Generate Allure Report

```bash
allure serve results/allure-results
```

---

## Continuous Integration

The project includes a **GitHub Actions** workflow that automatically:

- Installs project dependencies
- Installs Playwright browsers
- Executes the test suite
- Uploads Allure test results as artifacts

---

## Notes

This project was developed for learning purposes during my QA internship at **Kafein Technology**, using the Swag Labs demo application.
