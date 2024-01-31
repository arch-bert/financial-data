# Financial Data Extractor

This Python script allows users to extract financial data for stocks, cryptocurrencies, and forex rates. The data can be fetched for different intervals and exported in various formats.

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

