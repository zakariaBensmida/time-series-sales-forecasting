"""Unit tests for data_loader."""

import pytest
import pandas as pd
from src.data_loader import load_and_preprocess_data
from pathlib import Path

def test_load_and_preprocess_data(tmp_path: Path) -> None:
    """Test data loading and preprocessing."""
    # Create sample CSV
    sample_data = pd.DataFrame(
        {
            "Order Date": ["2023-01-01", "2023-01-02"],
            "Sales": [100, 200],
        }
    )
    csv_path = tmp_path / "train.csv"
    sample_data.to_csv(csv_path, index=False)

    # Run function
    df = load_and_preprocess_data(csv_path)

    # Assertions
    assert not df.empty
    assert "date" in df.columns
    assert "Sales" in df.columns
    assert "day_of_week" in df.columns