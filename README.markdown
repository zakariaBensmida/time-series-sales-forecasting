# Time Series Sales Forecasting

Sales forecasting using the Kaggle Superstore Sales dataset with ARIMA, Prophet, Random Forest, LSTM, and ensemble models. Includes a Streamlit dashboard and optional AWS deployment.

## Features
- Processes daily sales data with feature engineering.
- Forecasts sales using multiple models.
- Visualizes trends and predictions via Streamlit.
- Optional S3 upload for results.
- Includes type hints, docstrings, linting, tests, and CI.

## Prerequisites
- Python 3.8+ (https://www.python.org/downloads/)
- Kaggle account (https://www.kaggle.com/)
- Windows with Command Prompt
- Optional: AWS account for S3

## Setup
1. **Clone Repository**:
   cmd
   git clone https://github.com/your-username/time-series-sales-forecasting.git
   cd time-series-sales-forecasting
   

2. **Create Virtual Environment**:
   cmd
   python -m venv .venv
   .venv\Scripts\activate


3. **Install Dependencies**:
   cmd
   pip install -r requirements.txt
   

4. **Download Kaggle Dataset**:
   - Visit https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting
   - Download `train.csv`
   - Create `data/raw/`:
     cmd
     mkdir data\raw
     
   - Place `train.csv` in `data/raw/`

5. **Configure Environment**:
   - Copy `.env.example`:
     cmd
     copy .env.example .env
     
   - Edit `.env` in Notepad:
     plaintext
     DATA_DIR=data
     AWS_ACCESS_KEY_ID=
     AWS_SECRET_ACCESS_KEY=
     AWS_REGION=
     

## Running
1. **Format Code**:
   cmd
   black .
   ruff check --fix .
   

2. **Run Analysis**:
      cmd
   python main.py

   - Generates `output/sales_predictions.csv`

3. **Launch Dashboard**:
      cmd
   streamlit run src/dashboard.py

   - Opens http://localhost:8501

4. **Optional AWS**:
   - Add AWS credentials to `.env`
   - Upload:
     cmd
     python src/aws_utils.py output/sales_predictions.csv your-bucket sales_predictions.csv
     

## Troubleshooting
- **Browser Errors**: Ensure files (`README.md`, `src/dashboard.py`) are in correct paths, use Chrome/Edge.
- **FileNotFoundError**: Verify `train.csv` in `data/raw/`, `.env` has `DATA_DIR=data`.
- **ModuleNotFoundError**: Reinstall dependencies: `pip install -r requirements.txt`.

## Structure

time-series-sales-forecasting/
├── src/                    # Code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── forecasting.py
│   ├── dashboard.py
│   ├── aws_utils.py
├── tests/                  # Tests
│   ├── __init__.py
│   ├── test_data_loader.py
├── notebooks/              # Notebooks
│   ├── exploratory_analysis.ipynb
├── data/raw/               # Kaggle data
├── output/                 # Results
├── .env                    # Local settings
├── .env.example            # Template
├── .gitignore              # Git rules
├── .ruff.toml              # Linting
├── requirements.txt        # Dependencies
├── main.py                 # Main script
```

## License
MIT

## Contact
[zakaria bensmida] (zakariaibensmida@gmail.com)
