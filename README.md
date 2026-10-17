#FINE3300 Assignment #1: Exchange Rate Calculator

## Project Description
This repository contains the Python source code and data for The exchange rate calculator. It uses object-oriented programing to read the annual exchange rate data published by the Bank of Canada and converts monetary amounts between Canadian Dollars (CAD) and United States Dollars (USD) using the most recent FXAUSDCAD exchange rate.

## Repository Structure
* `Calculator.py` — Object-oriented Python program written without AI that parses the CSV file, extracts the latest FXAUSDCAD rate from the last row, prompts the user via input(), and displays the formatted conversion.
* `ExchangeRatesAI.py` — Python program generated using an LLM (Gemini 3.1 Pro) that accomplishes the same task.
* `BankOfCanadaExchangeRate.2026.csv` — Bank of Canada annual exchange rate dataset (2017–2025).