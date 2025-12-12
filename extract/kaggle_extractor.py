"""Extract financial data from Kaggle dataset."""

import os
import pandas as pd
from pathlib import Path
import requests
import zipfile

class KaggleExtractor:
    """Extract financial data from Kaggle."""
    
    def __init__(self, dataset_name="nazaninmottaghi2022/financial-data"):
        self.dataset_name = dataset_name
        self.raw_data_path = Path("data/raw")
        self.raw_data_path.mkdir(parents=True, exist_ok=True)
        
    def download_dataset(self):
        """Download dataset from Kaggle using Kaggle API."""
        print(f"Downloading dataset: {self.dataset_name}")
        
        try:
            # Using Kaggle API to download
            import kaggle
            kaggle.api.dataset_download_files(
                self.dataset_name,
                path=self.raw_data_path,
                unzip=True
            )
            print("Dataset downloaded successfully!")
            return True
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            return False
    
    def extract_csv_files(self):
        """Extract CSV files from downloaded data."""
        csv_files = list(self.raw_data_path.glob("*.csv"))
        
        if not csv_files:
            print("No CSV files found in raw data directory.")
            return None
        
        print(f"Found {len(csv_files)} CSV file(s):")
        for file in csv_files:
            print(f"  - {file.name}")
        
        return csv_files
    
    def read_financial_data(self, filename="financial_data.csv"):
        """Read the main financial dataset."""
        file_path = self.raw_data_path / filename
        
        if not file_path.exists():
            print(f"File {filename} not found. Attempting to download...")
            if not self.download_dataset():
                return None
        
        try:
            df = pd.read_csv(file_path)
            print(f"\nLoaded {filename}:")
            print(f"  - Shape: {df.shape}")
            print(f"  - Columns: {list(df.columns)}")
            return df
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

if __name__ == "__main__":
    # Example usage
    extractor = KaggleExtractor()
    
    # Download and extract
    extractor.download_dataset()
    csv_files = extractor.extract_csv_files()
    
    # Read main financial data
    df = extractor.read_financial_data()
    if df is not None:
        print("\nFirst few rows:")
        print(df.head())
