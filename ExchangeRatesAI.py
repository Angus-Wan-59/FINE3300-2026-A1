"""
FINE 3300 - Fall 2026: Assignment #1 (Part 2 - Vibe Coding)
File: ExchangeRatesAI.py
Description: AI-generated currency converter class using csv.DictReader, 
context managers, and type annotations to convert between USD and CAD.
"""

import csv


class ExchangeRates:
    """
    Reads Bank of Canada exchange rate CSV files and performs 
    currency conversions between USD and CAD.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initializes the ExchangeRates instance and loads the latest USD/CAD rate.
        """
        self.filepath: str = filepath
        self.usd_to_cad_rate: float = self._extract_latest_usd_cad_rate()

    def _extract_latest_usd_cad_rate(self) -> float:
        """
        Reads the CSV file using csv.DictReader and extracts the FXAUSDCAD rate 
        from the final row of data.
        """
        with open(self.filepath, mode="r", encoding="utf-8-sig", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            if not rows:
                raise ValueError("The provided CSV file contains no data rows.")
            
            latest_row = rows[-1]
            return float(latest_row["FXAUSDCAD"])

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        """
        Converts a monetary amount between USD and CAD based on the latest rate.
        """
        source = from_currency.strip().upper()
        target = to_currency.strip().upper()

        if source == target:
            return amount
        elif source == "USD" and target == "CAD":
            return amount * self.usd_to_cad_rate
        elif source == "CAD" and target == "USD":
            return amount / self.usd_to_cad_rate
        else:
            raise ValueError(f"Unsupported currency pair: {source} to {target}")


def main() -> None:
    # Initialize the exchange rate calculator with the dataset
    data_file = "BankOfCanadaExchangeRate.2026.csv"
    converter = ExchangeRates(data_file)

    # Prompt user for conversion details
    raw_amount = input("Enter the amount to convert: ")
    cleaned_amount = float(raw_amount.replace("$", "").replace(",", "").strip())
    from_curr = input("Enter the 'from' currency (USD or CAD): ").strip().upper()
    to_curr = input("Enter the 'to' currency (USD or CAD): ").strip().upper()

    # Calculate and display formatted output
    converted_value = converter.convert(cleaned_amount, from_curr, to_curr)
    print(f"${cleaned_amount:,.2f} {from_curr} = ${converted_value:,.2f} {to_curr}")


if __name__ == "__main__":
    main()