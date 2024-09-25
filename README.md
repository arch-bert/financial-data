# Financial Data Extractor

This Python script allows users to extract financial data for stocks, cryptocurrencies, and forex rates. The data can be fetched for different intervals and exported in various formats.

## Features

- **Multi-Asset Support**: Fetch data for stocks, cryptocurrencies, and forex pairs.
- **Flexible Intervals**: Supports daily, weekly, monthly, and intraday intervals (e.g., 1min, 5min).
- **Custom Date Range**: Specify custom start and end dates for data retrieval.
- **Multiple Output Formats**: Export data to CSV, Excel (XLSX), or JSON formats.
- **Command-Line Interface**: Use command-line arguments for quick data extraction.
- **Interactive Mode**: Guided input prompts for parameter selection.

## Installation and Setup

### 1. Install OpenBB Terminal

Install OpenBB Terminal using pip:

```bash
pip install openbb_terminal
```

### 2. Set API keys

- **Register with Financial Data Providers:** Sign up on their respective websites for services such as Alpha Vantage, Financial Modeling Prep, or others depending on your data needs.

- **Generate API Keys:** After account creation, generate your API keys typically found under account settings or a dedicated API section.

- **Enter API Keys in OpenBB Terminal:** After generating your API keys, you will need to enter these keys into the OpenBB Terminal, using:

```bash
/keys <service_name> <api_key>
```
Here, `<service_name>` is the identifier for the financial data service (like alphavantage, iex, coinmarketcap, etc.), and `<api_key>` is the actual API key you obtained from the service.

### 3. Install OpenBB's SDK

- **Install miniconda** from https://docs.conda.io/projects/miniconda/en/latest/

- **Create the environment** using a configuration file from the OpenBB Terminal repository. In miniconda terminal, run:

```bash
conda env create -n obb --file https://raw.githubusercontent.com/OpenBB-finance/OpenBBTerminal/main/build/conda/conda-3-9-env.yaml
```

- **Activate the (obb) environment:** In miniconda terminal, run:

```bash
conda activate obb
```

- **Install OpenBB SDK** by running:
```bash
pip install "openbb[optimization]==3.2.4" --no-cache-dir
```
and
```bash
pip install "openbb[forecast]==3.2.4" --no-cache-dir
```

- **Configure Your IDE:** In your Integrated Development Environment (IDE), such as Visual Studio Code, set the Python interpreter to the 'obb' environment. In VS Code, you can do this by pressing Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the Command Palette, then typing and selecting 'Python: Select Interpreter', and finally choosing the 'obb' environment from the list.

## Usage

The Financial Data Extractor can be used in two ways: via command-line arguments or interactive mode.

#### Command-Line Arguments

You can pass arguments directly when running the script:
```bash
python main.py <data_type> <symbol> <start_date> <end_date> <interval> <format>
```
Example:
```bash
python main.py stocks AAPL 2022-01-01 2022-01-31 daily csv
```

#### Interactive Mode

If no command-line arguments are provided, the script will prompt you for input:

1. **Select Data Type:** Choose from stocks, crypto, or forex.
2. **Enter Symbol:**
- Stocks: Ticker symbol (e.g., AAPL)
- Crypto: Cryptocurrency symbol (e.g., BTC)
- Forex: Currency pair in FROM/TO format (e.g., USD/EUR)
3. **Enter Start Date:** In YYYY-MM-DD format.
4. **Enter End Date:** In YYYY-MM-DD format.
5. **Select Interval:** Choose from 1min, 5min, 15min, 30min, 60min, daily, weekly, or monthly.
6. **Select Output Format:** Choose from csv, xlsx, or json.

## Project Structure
```
financial-data-extractor/
├── src/
│   ├── crypto/
│   │   └── crypto_prices.py
│   ├── currency/
│   │   └── forex_rates.py
│   ├── stocks/
│   │   └── stock_prices.py
│   ├── utils/
│   │   ├── data.py
│   │   └── suppress_print.py
│   └── main.py
├── output/  # Generated output files will be stored here
├── README.md
├── requirements.txt
└── LICENSE
```