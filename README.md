# Stock Trend Prediction Web App

## Project Overview

This project is a Streamlit-based web application designed to visualize historical stock data and predict future stock trends using a pre-trained Keras deep learning model. Users can input any stock ticker symbol (e.g., AAPL, GOOGL, MSFT) to view its historical performance, moving averages, and a comparison of predicted vs. actual closing prices.

## Features

* **Interactive Stock Ticker Input:** Easily search for any stock by its ticker symbol.
* **Historical Data Overview:** Displays a statistical summary of the stock's historical data from 2010 to 2024.
* **Trend Visualizations:**
    * Closing Price vs. Time chart.
    * Closing Price vs. Time with 100-day Moving Average (MA).
    * Closing Price vs. Time with 100-day MA and 200-day MA, providing insights into short-term and long-term trends.
* **Stock Price Prediction:** Leverages a deep learning model to forecast future stock closing prices.
* **Prediction vs. Original Comparison:** Visualizes the predicted prices against the actual historical prices for easy comparison and model evaluation.

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For creating the interactive web application user interface.
* **Keras:** For building and loading the deep learning model.
* **TensorFlow:** (Implied by Keras) For the underlying deep learning framework.
* **NumPy:** For numerical operations and array manipulation.
* **Pandas:** For data manipulation and analysis, especially with DataFrames.
* **Matplotlib:** For creating static, animated, and interactive visualizations.
* **yfinance:** For fetching historical stock market data.
* **Scikit-learn:** For data preprocessing (MinMaxScaler).

## Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

* Python 3.7+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ATHvc/Stock_trend_prediction.git]
    cd Stock_trend_prediction
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Create a `requirements.txt` file in your project's root directory with the following content:
    ```
    numpy>=1.20
    pandas>=1.3
    matplotlib>=3.4
    streamlit>=1.0
    yfinance>=0.1.70
    keras>=2.0
    tensorflow>=2.0 # Keras now typically runs on TensorFlow
    scikit-learn>=1.0
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Place the Pre-trained Model:**
    Ensure you have your pre-trained Keras model file named `keras_model.h5` in the root directory of your project. If you need to train a new model, you'll need a separate script for that.

### Running the Application

1.  **Navigate to the project directory:**
    ```bash
    cd Stock_trend_prediction
    ```

2.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

3.  The application will open in your default web browser (usually at `http://localhost:8501`).

## Usage

1.  Upon launching the app, you will see a text input field labeled "Enter Stock Ticker".
2.  Type the ticker symbol of the stock you want to analyze (e.g., `AAPL` for Apple Inc., `GOOGL` for Alphabet Inc., `TSLA` for Tesla Inc.).
3.  Press Enter, and the app will automatically fetch the data, display charts, and show predictions.


## License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.

## Contact

If you have any questions or feedback, feel free to reach out:

* **GitHub:** [https://github.com/ATHvc]
* **Email:** [atharvachinchalkar007@gmail.com]

---
*Developed by [ATHvc]*
