# tax-system-pytest-examples

**NOTE:** This repository is intended for educational purposes, specifically to practice and demonstrate unit testing with `pytest` on a taxation system.

A Python package for calculating personal income tax in the fictional country of Bobolia, including support for "badbob" adjustments and progressive tax brackets.

> **Attribution:**  
> The logic in the `src/` directory was originally authored by [unclebob] [https://github.com/unclebob]
> This repository was created to practice and demonstrate unit test writing using `pytest`.

## Features

- **Progressive Tax Brackets:** Calculates base tax using multiple income brackets.
- **BadBob Adjustments:** Applies special adjustments for class 1 and class 2 "badbob" purchases.
- **Comprehensive Testing:** Includes pytest-based unit tests for all major tax scenarios.

## Project Structure

```
tax-system-pytest-examples/
│
├── src/
│   ├── tax_bracketter.py      # Base tax calculation logic
│   ├── badbob_adjuster.py     # Badbob adjustment logic
│   └── tax_calculator.py      # Main tax calculation orchestration
│
└── tests/
    ├── test_tax_bracketter.py # Unit tests for tax brackets
    └── test_tax_calculator.py # Unit tests for full tax calculation
```

## Usage

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/tax-system-pytest-examples.git
    cd tax-system-pytest-examples
    ```

2. **Install dependencies (if any):**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the tests:**
    - From the project root:
        ```sh
        pytest -v
        ```
    - Or, if running from the `tests` directory, set the `PYTHONPATH`:
        ```sh
        # Windows PowerShell
        $env:PYTHONPATH = ".."
        pytest -v
        ```

## License

MIT License

---

*This project is for educational and demonstration purposes only.*