# Automation Developer Skill Test: Rule-Based Synthetic Data Generator

## Project Overview

This project is a Python-based tool built to fulfill the requirements of the Automation Developer skill test. More than just a script, this is a demonstration of a configurable, rule-based synthetic data generator designed specifically for a FinTech QA environment.

The tool generates a list of realistic stock trade transactions, applies multiple layers of business logic, and exports the data to a professionally formatted Excel report. The key feature is its ability to generate data for specific QA scenarios (e.g., normal market activity, high-volume failures), making it a practical tool for automating validation and streamlining testing workflows.

## Core Features & Demonstrated Skills

This project was built to directly showcase the key skills and responsibilities outlined in the job description.

- **Rule-Based Synthetic Data Generation**: The core of the tool is a submodel that generates realistic data based on defined rules. A user can easily select a scenario—like `"high_volume_failures"` or `"institutional_trades"`—to generate a dataset tailored for specific testing needs.
- **Multi-Layered Logical Operations**: The script demonstrates the ability to turn business rules into code by applying several logical operations:
  - A simple derived column (`Trade Value` = `Quantity` \* `Trade Price`).
  - A complex, multi-conditional derived column (`Flagged for Review`) to simulate a compliance or risk check.
- **Automated QA Highlighting**: To help testers "speed up releases" and "maintain product reliability", the tool uses conditional formatting to automatically highlight high-risk data:
  - **Red Highlight**: Applied to rows with a `FAILED` status.
  - **Yellow Highlight**: Applied to rows where the `Trade Value` exceeds a defined risk threshold.
- **Advanced Data Processing & Styling**: The project leverages the required libraries to handle data from creation to final presentation:
  - **pandas**: Used for initial data structuring, transformation, and creating derived columns.
  - **openpyxl**: Used for advanced Excel manipulation, including applying header styles, cell formats (currency), and sophisticated conditional formatting rules.
- **Professional Project Structure**: The inclusion of this `README.md` and a `requirements.txt` file demonstrates a commitment to documentation and best practices for collaboration, aligning with the need for experience using GitHub for version control.

## How to Run the Tool

### Prerequisites

- Python 3.10+
- `pip` (Python package installer)

### 1. Setup Environment

It is recommended to use a virtual environment to manage dependencies.

```sh
# Create a virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

Install all required libraries from the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

### 3. Execute the Script

Run the script from your terminal. The output will be a file named `output.xlsx` in the same directory.

```sh
python generate_excel.py
```

## Understanding the Scenarios

This tool is designed to be useful for a QA team. By changing a single line in the `main()` function of the script, a user can generate different datasets to test specific conditions:

- **`standard_day`**: For general regression testing with mostly successful trades.
- **`high_volume_failures`**: To stress-test the system's error handling, logging, and alerting capabilities.
- **`institutional_trades`**: To test for numerical overflow bugs and correct handling of large-value transactions.

This configurability demonstrates an understanding of building reusable automation tools that reduce manual work.
