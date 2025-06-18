# Time Series Analysis

This repository contains Jupyter Notebooks and code for learning and experimenting with time series analysis concepts using Python. The work includes statistical tests, model simulation, and practical application to real-world datasets such as financial market data and production series.

## Contents

- **ARIMA_Model.ipynb**  
  Demonstrates the use of ARIMA (AutoRegressive Integrated Moving Average) and ARMA models for simulating stock trading strategies using historical price data (e.g., Apple Inc. - AAPL). Includes visualization of returns, ACF/PACF plots, and a simulation function for buy/sell strategies.

- **Augmented_Dickey_Fuller_Test_.ipynb**  
  Explains and demonstrates the Augmented Dickey-Fuller (ADF) test for stationarity. Includes code to generate AR(1) and AR(2) processes (stationary and non-stationary) and visualize their behavior and test results.

- **Time_series_analysis.ipynb**  
  Tutorial notebook that loads and explores a monthly ice cream production time series and SPY (S&P 500 ETF) stock prices. Includes ACF and PACF analysis, plotting, and data preparation steps.

## Features

- Statistical tests for time series stationarity
- ARIMA/ARMA modeling and simulation
- Custom simulation of trading strategies
- Visualizations: line plots, ACF (Autocorrelation Function), PACF (Partial Autocorrelation Function)
- Use of real-world datasets (Yahoo Finance, CSV data)

## Requirements

- Python 3.x
- Jupyter Notebook
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `tqdm`
  - `statsmodels`
  - `yfinance`
  - `scipy`

You can install the required libraries with:

```bash
pip install numpy pandas matplotlib seaborn tqdm statsmodels yfinance scipy
```

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/ATHvc/Time_Series_Analysis.git
    ```
2. Open the desired notebook(s) with Jupyter Notebook or Jupyter Lab:
    ```bash
    jupyter notebook
    ```
3. Run the code cells in order. For `Time_series_analysis.ipynb`, ensure that `ice_cream.csv` is present in the working directory.

## References

- [Statsmodels Documentation](https://www.statsmodels.org/)
- [Yahoo Finance Python API](https://pypi.org/project/yfinance/)
- [ADF Test Explanation - Wikipedia](https://en.wikipedia.org/wiki/Augmented_Dickey–Fuller_test)
- [ARIMA Model Explanation - Wikipedia](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average)

## License

This repository is for educational and research purposes. See the `LICENSE` file (if present) for usage terms.

---

*Created and maintained by [ATHvc](https://github.com/ATHvc)*
To run the notebooks, install the following libraries:

```bash
pip install pandas numpy matplotlib seaborn statsmodels
