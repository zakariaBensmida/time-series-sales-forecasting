"""Main script for sales forecasting analysis."""

import logging
from pathlib import Path
from src.data_loader import load_and_preprocess_data
from src.forecasting import train_and_forecast

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """Run the sales forecasting pipeline."""
    logger.info("Starting sales forecasting analysis")

    # Load and preprocess data
    data_dir = Path("data")
    try:
        df = load_and_preprocess_data(data_dir / "raw" / "train.csv")
        logger.info("Data loaded and preprocessed")
    except Exception as e:
        logger.error(f"Failed to load data: {e}")
        return

    # Train models and forecast
    try:
        predictions_df, metrics_df = train_and_forecast(df)
        logger.info("Forecasting complete")
    except Exception as e:
        logger.error(f"Forecasting failed: {e}")
        return

    # Save results
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    predictions_df.to_csv(output_dir / "sales_predictions.csv", index=False)
    metrics_df.to_csv(output_dir / "model_metrics.csv", index=False)
    logger.info(f"Results saved to {output_dir}")


if __name__ == "__main__":
    main()
