"""Train and forecast sales using multiple models."""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

def train_and_forecast(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Train models and generate forecasts.

    Args:
        df: Preprocessed DataFrame with date and Sales

    Returns:
        Tuple of predictions DataFrame and metrics DataFrame
    """
    try:
        # Prepare data
        train_size = int(0.8 * len(df))
        train_df = df.iloc[:train_size]
        test_df = df.iloc[train_size:]

        # Simple Random Forest model
        X_train = train_df[["day_of_week", "month"]]
        y_train = train_df["Sales"]
        X_test = test_df[["day_of_week", "month"]]
        y_test = test_df["Sales"]

        model = RandomForestRegressor(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        # Combine predictions
        predictions_df = test_df[["date", "Sales"]].copy()
        predictions_df["rf_prediction"] = predictions

        # Calculate metrics
        mape = mean_absolute_percentage_error(y_test, predictions) * 100
        rmse = np.sqrt(mean_squared_error(y_test, predictions))
        metrics_df = pd.DataFrame(
            {
                "Model": ["RandomForest"],
                "MAPE": [mape],
                "RMSE": [rmse],
            }
        ).set_index("Model")

        logger.info("Forecasting completed successfully")
        return predictions_df, metrics_df
    except Exception as e:
        logger.error(f"Forecasting failed: {e}")
        raise