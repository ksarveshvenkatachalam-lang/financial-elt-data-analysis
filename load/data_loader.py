"""Load financial data into structured format."""

import pandas as pd
import sqlite3
from pathlib import Path
from sqlalchemy import create_engine
import json

class DataLoader:
    """Load extracted financial data into database or structured format."""
    
    def __init__(self, db_path="data/processed/financial_data.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        
    def load_to_sqlite(self, df, table_name="financial_data"):
        """Load DataFrame to SQLite database."""
        try:
            df.to_sql(table_name, self.engine, if_exists='replace', index=False)
            print(f"Data loaded to table '{table_name}' successfully!")
            print(f"Total rows loaded: {len(df)}")
            return True
        except Exception as e:
            print(f"Error loading data to database: {e}")
            return False
    
    def load_to_csv(self, df, filename="processed_financial_data.csv"):
        """Save DataFrame to CSV in processed folder."""
        output_path = Path("data/processed") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            df.to_csv(output_path, index=False)
            print(f"Data saved to: {output_path}")
            print(f"File size: {output_path.stat().st_size / 1024:.2f} KB")
            return output_path
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return None
    
    def load_to_parquet(self, df, filename="financial_data.parquet"):
        """Save DataFrame to Parquet format for efficient storage."""
        output_path = Path("data/processed") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            df.to_parquet(output_path, index=False, compression='snappy')
            print(f"Data saved to Parquet: {output_path}")
            print(f"File size: {output_path.stat().st_size / 1024:.2f} KB")
            return output_path
        except Exception as e:
            print(f"Error saving to Parquet: {e}")
            return None
    
    def validate_loaded_data(self, table_name="financial_data"):
        """Validate data loaded in database."""
        try:
            query = f"SELECT COUNT(*) as count FROM {table_name}"
            result = pd.read_sql(query, self.engine)
            print(f"\nValidation Results:")
            print(f"  - Total records in '{table_name}': {result['count'].iloc[0]}")
            
            # Show sample data
            sample_query = f"SELECT * FROM {table_name} LIMIT 5"
            sample_df = pd.read_sql(sample_query, self.engine)
            print(f"\nSample data:")
            print(sample_df)
            
            return True
        except Exception as e:
            print(f"Error validating data: {e}")
            return False

if __name__ == "__main__":
    # Example usage
    from extract.kaggle_extractor import KaggleExtractor
    
    # Extract data
    extractor = KaggleExtractor()
    df = extractor.read_financial_data()
    
    if df is not None:
        # Load data
        loader = DataLoader()
        
        # Load to SQLite
        loader.load_to_sqlite(df)
        
        # Load to CSV
        loader.load_to_csv(df)
        
        # Validate
        loader.validate_loaded_data()
