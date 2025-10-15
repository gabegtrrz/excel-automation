import pandas as pd
import numpy as np
from faker import Faker
import random
import uuid
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

### Configuration
NUM_RECORDS = 50
OUTPUT_FILE_NAME = 'output.xlsx'
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


def main():
    pass

