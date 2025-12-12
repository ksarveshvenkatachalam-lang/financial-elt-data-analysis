"""Transform and enrich financial data."""

import pandas as pd
import numpy as np
from datetime import datetime

class DataTransformer:
    """Transform financial data with calculations and feature engineering."""
    
    def __init__(self):
        self.transformed_df = None
        
    def clean_data(self, df):
        """Clean and prepare data."""
        print("Cleaning data...")
        df_clean = df.copy()
        
        # Convert date column to datetime
        if 'Date' in df_clean.columns:
            df_clean['Date'] = pd.to_datetime(df_clean['Date'])
            df_clean = df_clean.sort_values('Date')
        
        # Handle missing values
        print(f"Missing values before cleaning:")
        print(df_clean.isnull().sum())
        
        # Forward fill for financial data
        df_clean = df_clean.fillna(method='ffill')
        
        print(f"\nMissing values after cleaning:")
        print(df_clean.isnull().sum())
        
        return df_clean
    
    def add_time_features(self, df):
        """Add time-based features."""
        print("\nAdding time features...")
        df_time = df.copy()
        
        if 'Date' in df_time.columns:
            df_time['Year'] = df_time['Date'].dt.year
            df_time['Month'] = df_time['Date'].dt.month
            df_time['Quarter'] = df_time['Date'].dt.quarter
            df_time['Day_of_Week'] = df_time['Date'].dt.dayofweek
            df_time['Week_of_Year'] = df_time['Date'].dt.isocalendar().week
            
            print(f"Added time features: Year, Month, Quarter, Day_of_Week, Week_of_Year")
        
        return df_time
    
    def calculate_returns(self, df):
        """Calculate daily returns for each asset."""
        print("\nCalculating returns...")
        df_returns = df.copy()
        
        # Define asset columns
        asset_columns = [col for col in df.columns if col not in ['Date', 'Year', 'Month', 'Quarter', 'Day_of_Week', 'Week_of_Year']]
        
        for col in asset_columns:
            if pd.api.types.is_numeric_dtype(df_returns[col]):
                # Calculate daily returns
                df_returns[f'{col}_Return'] = df_returns[col].pct_change() * 100
                
                # Calculate cumulative returns
                df_returns[f'{col}_Cumulative_Return'] = ((1 + df_returns[col].pct_change()).cumprod() - 1) * 100
                
                print(f"  - Calculated returns for {col}")
        
        return df_returns
    
    def calculate_moving_averages(self, df, windows=[7, 30, 90]):
        """Calculate moving averages."""
        print(f"\nCalculating moving averages for windows: {windows}...")
        df_ma = df.copy()
        
        asset_columns = [col for col in df.columns if col not in ['Date', 'Year', 'Month', 'Quarter', 'Day_of_Week', 'Week_of_Year'] 
                        and not col.endswith('_Return') and not col.endswith('_Cumulative_Return')]
        
        for col in asset_columns:
            if pd.api.types.is_numeric_dtype(df_ma[col]):
                for window in windows:
                    df_ma[f'{col}_MA_{window}'] = df_ma[col].rolling(window=window).mean()
                    print(f"  - {col}: {window}-day MA")
        
        return df_ma
    
    def calculate_volatility(self, df, window=30):
        """Calculate rolling volatility."""
        print(f"\nCalculating {window}-day rolling volatility...")
        df_vol = df.copy()
        
        # Find return columns
        return_columns = [col for col in df.columns if col.endswith('_Return') and not col.endswith('_Cumulative_Return')]
        
        for col in return_columns:
            asset_name = col.replace('_Return', '')
            df_vol[f'{asset_name}_Volatility_{window}d'] = df_vol[col].rolling(window=window).std()
            print(f"  - {asset_name}")
        
        return df_vol
    
    def add_price_ratios(self, df):
        """Add comparative price ratios between assets."""
        print("\nCalculating price ratios...")
        df_ratio = df.copy()
        
        # Example: Gold to Oil ratio
        if 'Gold' in df.columns and 'Oil' in df.columns:
            df_ratio['Gold_Oil_Ratio'] = df_ratio['Gold'] / df_ratio['Oil']
            print("  - Gold/Oil ratio")
        
        # Example: S&P 500 to NASDAQ ratio
        if 'S&P 500' in df.columns and 'NASDAQ' in df.columns:
            df_ratio['SP500_NASDAQ_Ratio'] = df_ratio['S&P 500'] / df_ratio['NASDAQ']
            print("  - S&P 500/NASDAQ ratio")
        
        return df_ratio
    
    def transform_pipeline(self, df):
        """Execute complete transformation pipeline."""
        print("="*50)
        print("Starting Data Transformation Pipeline")
        print("="*50)
        
        # Step 1: Clean
        df = self.clean_data(df)
        
        # Step 2: Time features
        df = self.add_time_features(df)
        
        # Step 3: Returns
        df = self.calculate_returns(df)
        
        # Step 4: Moving averages
        df = self.calculate_moving_averages(df)
        
        # Step 5: Volatility
        df = self.calculate_volatility(df)
        
        # Step 6: Price ratios
        df = self.add_price_ratios(df)
        
        self.transformed_df = df
        
        print("\n" + "="*50)
        print("Transformation Complete!")
        print("="*50)
        print(f"Final shape: {df.shape}")
        print(f"Total columns: {len(df.columns)}")
        
        return df

if __name__ == "__main__":
    # Example usage
    from extract.kaggle_extractor import KaggleExtractor
    
    # Extract data
    extractor = KaggleExtractor()
    df = extractor.read_financial_data()
    
    if df is not None:
        # Transform
        transformer = DataTransformer()
        transformed_df = transformer.transform_pipeline(df)
        
        print("\nTransformed data columns:")
        print(list(transformed_df.columns))
        print("\nSample of transformed data:")
        print(transformed_df.head())
