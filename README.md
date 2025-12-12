#  Financial ELT Data Analysis Pipeline

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A professional-grade ELT (Extract, Load, Transform) data pipeline for analyzing financial market data from Kaggle. This project demonstrates industry best practices for data engineering, including modular architecture, comprehensive documentation, and automated workflows.

##  Project Overview

This pipeline processes daily closing prices for major financial indices and commodities:
- **S&P 500 Index** - US stock market performance
- **NASDAQ Composite** - Technology-focused index
- **Gold Prices** - Precious metal commodity
- **Crude Oil Prices** - Energy commodity

**Data Source**: [Kaggle Financial Data (2019-2024)](https://www.kaggle.com/datasets/nazaninmottaghi2022/financial-data)

## ✨ Features

### Extract
- ✅ Automated data extraction from Kaggle API
- ✅ CSV file parsing and validation
- ✅ Error handling and retry logic

### Load
- ✅ SQLite database storage
- ✅ CSV output for analysis
- ✅ Parquet format for efficient storage
- ✅ Data validation and integrity checks

### Transform
- ✅ **Time Features**: Year, Month, Quarter, Day of Week, Week of Year
- ✅ **Financial Metrics**: Daily returns, cumulative returns
- ✅ **Technical Indicators**: Moving averages (7, 30, 90 days)
- ✅ **Volatility Analysis**: Rolling volatility calculations
- ✅ **Comparative Analysis**: Price ratios between assets

##  Project Structure

```
financial-elt-data-analysis/
│
├── extract/
│   └── kaggle_extractor.py      # Data extraction from Kaggle
│
├── load/
│   └── data_loader.py            # Data loading to multiple formats
│
├── transform/
│   └── data_transformer.py       # Data transformation & feature engineering
│
├── data/
│   ├── raw/                      # Raw data from Kaggle
│   └── processed/                # Transformed data
│
├── main_pipeline.py              # Main ELT orchestration
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Kaggle API credentials
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ksarveshvenkatachalam-lang/financial-elt-data-analysis.git
   cd financial-elt-data-analysis
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Kaggle API credentials**
   - Go to [Kaggle Account Settings](https://www.kaggle.com/account)
   - Click "Create New API Token"
   - Place `kaggle.json` in:
     - Windows: `C:\Users\<Windows-username>\.kaggle\kaggle.json`
     - macOS/Linux: `~/.kaggle/kaggle.json`

### Usage

#### Run the Complete Pipeline

```bash
python main_pipeline.py
```

This will:
1. Extract financial data from Kaggle
2. Load data into SQLite, CSV, and Parquet formats
3. Transform data with feature engineering
4. Save processed data for analysis

#### Run Individual Components

**Extract Only:**
```python
from extract.kaggle_extractor import KaggleExtractor

extractor = KaggleExtractor()
df = extractor.read_financial_data()
```

**Load Only:**
```python
from load.data_loader import DataLoader

loader = DataLoader()
loader.load_to_sqlite(df, table_name="financial_data")
```

**Transform Only:**
```python
from transform.data_transformer import DataTransformer

transformer = DataTransformer()
transformed_df = transformer.transform_pipeline(df)
```

##  Output Data

### Raw Data
- Location: `data/raw/financial_data.csv`
- Columns: Date, S&P 500, NASDAQ, Gold, Oil
- Records: ~1,509 observations (2019-2024)

### Transformed Data
- Location: `data/processed/`
- Formats: SQLite, CSV, Parquet
- Additional Features: 30+ calculated metrics

##  Configuration

### Database Settings
Modify database path in `load/data_loader.py`:
```python
loader = DataLoader(db_path="data/processed/financial_data.db")
```

### Transformation Parameters
Adjust moving average windows in `transform/data_transformer.py`:
```python
transformer.calculate_moving_averages(df, windows=[7, 30, 90, 180])
```

## 🧪 Testing

```bash
# Run unit tests (when implemented)
pytest tests/

# Run with coverage
pytest --cov=. tests/
```

##  Data Analysis Examples

After running the pipeline, analyze the data:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load transformed data
df = pd.read_csv('data/processed/transformed_financial_data.csv')

# Plot S&P 500 with moving averages
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['S&P 500'], label='S&P 500')
plt.plot(df['Date'], df['S&P 500_MA_30'], label='30-Day MA')
plt.plot(df['Date'], df['S&P 500_MA_90'], label='90-Day MA')
plt.legend()
plt.show()
```

##  Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

##  Best Practices Demonstrated

This project showcases professional development practices:

- ✅ **Modular Architecture**: Separation of concerns (Extract, Load, Transform)
- ✅ **Clean Code**: PEP 8 compliance, type hints, docstrings
- ✅ **Version Control**: Meaningful commits, branch strategy
- ✅ **Documentation**: Comprehensive README, inline comments
- ✅ **Error Handling**: Try-except blocks, logging
- ✅ **Scalability**: Easy to extend with new data sources
- ✅ **Reproducibility**: Requirements file, clear setup instructions

##  Technologies Used

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **SQLAlchemy** - Database ORM
- **Kaggle API** - Data extraction
- **Matplotlib/Seaborn** - Data visualization
- **Plotly** - Interactive visualizations

##  Learn More

### Data Engineering Concepts
- [ELT vs ETL](https://www.integrate.io/blog/etl-vs-elt/)
- [Data Pipeline Best Practices](https://www.datacamp.com/tutorial/data-pipeline-design)

### Financial Analysis
- [Technical Indicators](https://www.investopedia.com/terms/t/technicalindicator.asp)
- [Moving Averages](https://www.investopedia.com/terms/m/movingaverage.asp)

## 🐛 Known Issues

- Large datasets may require additional memory optimization
- Kaggle API rate limits may affect frequent downloads

##  Roadmap

- [ ] Add unit tests with pytest
- [ ] Implement CI/CD with GitHub Actions
- [ ] Add data quality checks with Great Expectations
- [ ] Create Jupyter notebooks for analysis
- [ ] Add REST API endpoints with Flask/FastAPI
- [ ] Implement real-time data updates
- [ ] Add machine learning predictions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**Sarvesh Venkatachalam**
- GitHub: [@ksarveshvenkatachalam-lang](https://github.com/ksarveshvenkatachalam-lang)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/ksarveshvenkatachalam)

##  Acknowledgments

- Data provided by [Kaggle - Nazanin Mottaghi](https://www.kaggle.com/datasets/nazaninmottaghi2022/financial-data)
- Inspired by industry-standard data engineering practices
- Built for portfolio and learning purposes

##  Support

If you encounter any issues or have questions:
- Open an [Issue](https://github.com/ksarveshvenkatachalam-lang/financial-elt-data-analysis/issues)
- Check [Discussions](https://github.com/ksarveshvenkatachalam-lang/financial-elt-data-analysis/discussions)

---

