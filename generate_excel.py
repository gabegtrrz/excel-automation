import pandas as pd
import numpy as np
from faker import Faker
import random
import uuid
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

### Configuration
TICKER_SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'INTC', 'AMD']

BASE_PRICES = {
    'AAPL' : 247.66,
    'GOOGL' : 245.45,
    'MSFT' : 513.57,
    'AMZN' : 216.39,
    'TSLA' : 429.24,
    'META' : 708.65,
    'NFLX' : 1215.35,
    'NVDA' : 180.03,
    'INTC' : 35.63,
    'AMD'  : 218.09
}

def generate_synthetic_trade_data(num_records, quantity_range, status_distribution):
    """
    Generates a list of synthetic financial trade data records based on specific rules as a rule-based submodel.

    Args:
        num_records (int): Number of trade records to generate.
        quantity_range (tuple): Min and max quantity for trades.
        status_distribution (dict): dictionary defining the weighted distribution of statuses.

    - Uses Numpy for numerical data.
    - Uses Faker for realistic, non-numerical metadata (Source IP).
    """

    ### Initialization
    fake = Faker()
    trade_data = []
    statuses = list(status_distribution.keys())
    weights = list(status_distribution.values())


    for _ in range(num_records):
        ticker = random.choice(TICKER_SYMBOLS)
        base_price = BASE_PRICES[ticker]

        trade_price = round(np.random.normal(loc=base_price, scale=1.5), 2)
        quantity = np.random.randint(low=quantity_range[0], high=quantity_range[1])

        trade_status = random.choices(statuses, weights, k=1)[0] # always returns a list so take first element

        trade_data.append({
            'Trade ID': str(uuid.uuid4()),
            'Account ID': str(uuid.uuid4()),
            'Ticker': ticker,
            'Trade Type': random.choice(['BUY', 'SELL']),
            'Quantity': quantity,
            'Trade Price': trade_price,
            'Status': trade_status,
            'Source IP': fake.ipv4()
        })
    return trade_data

def apply_excel_formatting(excel_file):
    """Applies professional formatting to the Excel file for an easy-to-read report."""

    # Load workbook and select active sheet
    wb = load_workbook(excel_file)
    ws = wb.active

    if ws is None:
        print(f"Error: No active worksheet found in '{excel_file}'. Cannot apply formatting.")
        return

    # Styles
    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="0a3e7d", end_color="0a3e7d", fill_type="solid")
    center_align = Alignment(horizontal="center", vertical="center")
    
    for cell in ws[1]:
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align

    for col_idx, all_col_cells in enumerate(ws.columns, 1):

        # Format currency columns
        column_header = ws.cell(row=1, column=col_idx).value
        if column_header in ['Trade Price', 'Trade Value']:
            for cell in all_col_cells[1:]:
                cell.number_format = '$#,##0.00'

        # Auto-adjust column width
        max_length = 0
        column_letter = get_column_letter(col_idx)
        for cell in all_col_cells:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column_letter].width = adjusted_width

    wb.save(excel_file)
    print(f"Applied formatting to '{excel_file}'.")

    return 




def main():
    """Main function to define rules, select a scenario, and generate the data. This demonstrates building a configurable tool.
    """

    print("Starting Trade Data Excel File Generation...")

    ### Configuration
    NUM_RECORDS = 100
    OUTPUT_FILENAME = 'output.xlsx'
    
    ### Define Rules for QA Scenario ###

    scenarios = {
        'standard day': {
            'quantity_range': (10, 5001),
            'status_distribution': {'EXECUTED': 95, 'PENDING': 4, 'FAILED': 1}
        },
        'high_volume_failures': {
            'quantity_range': (100, 10001),
            'status_distribution': {'EXECUTED': 60, 'PENDING': 10, 'FAILED': 30}
        },
        'institutional_trades': {
            'quantity_range': (50000, 200001), # testing large numbers
            'status_distribution': {'EXECUTED': 98, 'PENDING': 2, 'FAILED': 0}
        },
    }

    ### Select Scenario to run ###
    # QA tester would change this to get different data according to their needs
    selected_scenario_name = 'standard day'
    selected_scenario = scenarios[selected_scenario_name] # to double-check

    print(f"Generating excel data for scenario: \n \n {selected_scenario}... \n")

    trade_data = generate_synthetic_trade_data(
        num_records=NUM_RECORDS,
        quantity_range=selected_scenario['quantity_range'],
        status_distribution=selected_scenario['status_distribution']
    )

    ### Process and save data to Excel
    df = pd.DataFrame(trade_data)
    df['Trade Value'] = df['Trade Price'] * df['Quantity']
    df = df[['Trade ID', 'Ticker', 'Trade Type', 'Trade Price', 'Quantity','Trade Value', 'Status', 'Source IP']]

    df.to_excel(OUTPUT_FILENAME, index=False, sheet_name=selected_scenario_name)
    print(f"Successfully generated '{OUTPUT_FILENAME}'.")

    apply_excel_formatting(excel_file=OUTPUT_FILENAME)
    print("Script finished successfully!")



if __name__ == "__main__":
    main()
