# Automation Developer Skill Test: Rule-Based Synthetic Data Generator

## Project Overview

This project is a Python-based tool built to fulfill the requirements of the Automation Developer skill test. More than just a script, this is a demonstration of a configurable tool designed to **generate synthetic data, automate validation, and streamline reporting workflows** within a FinTech QA environment.



---

## Skill Test Checklist

This project successfully fulfills all requirements outlined in the skill test guidelines:

* **✅ Create an Excel file with a structured layout.**
    * The script automatically generates an Excel file named `output.xlsx`. The layout is structured with professionally styled headers and formatted data cells (e.g., currency), demonstrating the use of `openpyxl` for advanced styling.

* **✅ Include sample data.**
    * This requirement was exceeded by generating a configurable number of rows of realistic, rule-based synthetic data using NumPy and Faker, which is more practical for real-world QA testing.

* **✅ Apply at least one logical operation.**
    * This requirement was significantly exceeded by implementing multiple layers of testable code logic relevant to a FinTech environment:
        1.  **Derived Column:** A `Trade Value` column is calculated.
        2.  **Complex Derived Column:** A `Flagged for Review` column is added based on multi-conditional logic.
        3.  **Conditional Highlighting (Failures):** A visual logical operation highlights rows in red if the trade `Status` is `FAILED`.
        4.  **Conditional Highlighting (Risk):** A second visual rule highlights high-value trades in yellow.

* **✅ Save the file as `output.xlsx`.**
    * The script saves the final, formatted report as `output.xlsx` upon successful execution.

---

## Core Features & Demonstrated Skills

This project was built to directly showcase the key skills and responsibilities for the Automation Developer role.

* **Designed a Submodel for Realistic Synthetic Data**: The core of the tool is a function that **generates realistic synthetic data from defined rules**. A user can easily select a scenario—like `"high_volume_failures"`—to generate a dataset tailored for specific testing needs.

* **Turned Unclear Rules into Testable Code Logic**: The script implements multi-layered business logic, such as flagging trades for review and applying conditional formatting for failures, demonstrating the ability to transform requirements into **clean automation logic**.

* **Exceeded Bonus Point Requirements**: The tool explicitly uses the technologies mentioned as bonus criteria:
    * **Faker**: Used to generate realistic, non-numerical metadata (`Source IP`).
    * **NumPy Random Generation**: Used for all numerical data (`Quantity`, `Trade Price`) to ensure consistency.
    * **Simple Statistical Modeling**: Implemented using `np.random.normal()` to model realistic stock price fluctuations around a base value.

* **Used Pandas and Openpyxl for Data Handling**:
    * **Pandas**: Leveraged for data structuring, **validation, and transformation**, and for creating derived columns.
    * **Openpyxl**: Used for advanced Excel manipulation by **handling styles, formulas, and templates** (conditional formatting).

* **Structured for Team Collaboration**: The project includes this `README` to **document processes** and a `requirements.txt` file, demonstrating best practices for a **team setup** and collaborative workflows using **GitHub**.

## How to Run the Tool

### Prerequisites
* Python 3.10+
* `pip` (Python package installer)

### 1. Setup Environment
It is recommended to use a virtual environment.
```sh
# Create a virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Execute the Script
```sh
python generate_excel.py
```