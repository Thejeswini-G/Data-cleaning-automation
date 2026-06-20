# Data-cleaning-automation

## Project Overview
This project automates the process of cleaning a sales dataset, generating reports, and creating visualizations using Python. It demonstrates data preprocessing, report automation, and basic data analysis using the Pandas and Matplotlib libraries.

---

## Objectives
- Load sales data from a CSV file.
- Remove duplicate records.
- Handle missing values.
- Standardize text data.
- Generate summary statistics.
- Create sales visualization charts.
- Export cleaned data and reports to Excel.

---

## Technologies Used
- Python
- Pandas
- Matplotlib
- OpenPyXL

---

## Project Structure

```
Data_Cleaning_Reporting_Automation/
│── data/
│   └── sales_data.csv
│── reports/
│   ├── Cleaned_Data.xlsx
│   └── Summary_Report.xlsx
│── visuals/
│   └── sales_chart.png
│── main.py
```

---

## Features
- Reads sales data from a CSV file.
- Removes duplicate records.
- Handles missing values.
- Standardizes city names.
- Converts the Date column into datetime format.
- Generates summary statistics.
- Creates a bar chart of product sales.
- Saves cleaned data and reports automatically.

---

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

3. Place `sales_data.csv` inside the `data` folder.
4. Run the program:

```bash
python main.py
```

---

## Output
The project automatically generates:

- `reports/Cleaned_Data.xlsx`
- `reports/Summary_Report.xlsx`
- `visuals/sales_chart.png`

---

## Learning Outcome
This project provides hands-on experience in:
- Data Cleaning
- Data Preprocessing
- Report Automation
- Data Visualization
- Python Programming
- Working with CSV and Excel files

---

