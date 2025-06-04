
"""Load and preprocess sales data."""

import pandas as pd
from pathlib import Path
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger(__name__)

def load_and_preprocess_data(file_path: Path) -> pd.DataFrame:
    """Load and preprocess the Kaggle sales dataset.

    Args:
        file_path: Path to train.csv

    Returns:
        Preprocessed DataFrame
    """
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
        logger.info(f"Loaded data from {file_path}")

        # Basic preprocessing
        df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
        df = df.groupby("Order Date")["Sales"].sum().reset_index()
        df = df.rename(columns={"Order Date": "date", "Sales": "Sales"})
        df = df.sort_values("date")

        # Add simple features
        df["day_of_week"] = df["date"].dt.dayofweek
        df["month"] = df["date"].dt.month

        logger.info("Data preprocessed successfully")
        return df
    except Exception as e:
        logger.error(f"Preprocessing failed: {e}")
        raise
