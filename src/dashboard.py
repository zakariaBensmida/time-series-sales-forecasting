"""Streamlit dashboard for sales forecasting."""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

st.set_page_config(page_title="Sales Forecasting Dashboard", layout="wide")

def load_predictions() -> pd.DataFrame | None:
    """Load predictions from output file."""
    predictions_path = Path("output/sales_predictions.csv")
    if not predictions_path.exists():
        st.error("Run 'python main.py' to generate predictions.")
        logger.error(f"Missing: {predictions_path}")
        return None
    try:
        df = pd.read_csv(predictions_path)
        df["date"] = pd.to_datetime(df["date"])
        return df
    except Exception as e:
        st.error(f"Error loading predictions: {e}")
        logger.error(f"Load failed: {e}")
        return None

def main() -> None:
    """Run the dashboard."""
    st.title("Sales Forecasting Dashboard")
    st.markdown("Visualize sales forecasts.")

    predictions_df = load_predictions()
    if predictions_df is None:
        return

    # Metrics
    st.header("Key Metrics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Average Sales", f"${predictions_df['Sales'].mean():,.0f}")
    with col2:
        st.metric("Total Sales", f"${predictions_df['Sales'].sum():,.0f}")

    # Sales Trend
    st.header("Sales Trend")
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=predictions_df["date"],
            y=predictions_df["Sales"],
            mode="lines",
            name="Sales",
            line=dict(color="blue"),
        )
    )
    for col in [c for c in predictions_df.columns if c.endswith("_prediction")]:
        model_name = col.replace("_prediction", "").title()
        fig.add_trace(
            go.Scatter(
                x=predictions_df["date"],
                y=predictions_df[col],
                mode="lines",
                name=f"{model_name} Forecast",
                line=dict(dash="dash"),
            )
        )
    fig.update_layout(
        title="Sales vs Forecasts",
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        height=400,
    )
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()