import pandas as pd
import shutil
from pathlib import Path


def write_to_file(data_frame, file_name, format, output_dir='output'):
    """
    Writes a DataFrame to a file in the specified format.

    Parameters:
    data_frame (pd.DataFrame): The DataFrame to write.
    file_name (str): The base name of the file to write.
    format (str): The format to write the file in ('csv', 'xlsx', 'json').
    output_dir (str): The directory to write the file to (default is 'output').
    """

    # Make sure the output directory exists and is empty
    output_path = Path(output_dir)
    if output_path.exists():
        clear_directory(output_path)
    else:
        output_path.mkdir(parents=True)

    # Construct the file path
    file_path = output_path / f"{file_name}.{format}"

    try:
        # Save the DataFrame in the specified format
        if format == 'csv':
            data_frame.to_csv(file_path, index=True)

        elif format == 'xlsx':
            data_frame.to_excel(file_path, sheet_name='fin_data', index=True)

        elif format == 'json':
            data_frame.to_json(file_path)

        else:
            raise ValueError(f'{format} format is not supported.')

        print(f'Successfully written to {format} file: {file_path}')

    except Exception as e:
        print(f"Error writing file: {e}")


def clear_directory(dir_path):
    """
    Clears all files and directories in the specified directory.

    Parameters:
    dir_path (Path or str): The path to the directory to clear.
    """

    dir_path = Path(dir_path)

    if dir_path.is_dir():
        # Delete all files and sub-directories
        for item in dir_path.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()


def clean_data_frame(df):
    """
    Performs cleaning operations on a DataFrame.

    This function currently handles the following cleaning operations:
    - Renames the 'date' column to 'Date' for consistency.
    - Removes 'Adj Close', 'Dividends', and 'Stock Split' columns if they exist.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.

    Returns:
    None: The function modifies the DataFrame in place.
    """

    # Change 'date' column to 'Date'
    if 'date' in df.columns:
        df.rename(columns={'date': 'Date'}, inplace=True)

    # Remove 'Adj Close' Column
    if 'Adj Close' in df.columns:
        df.drop(columns='Adj Close', inplace=True)

    # Remove 'Dividends' Column
    if 'Dividends' in df.columns:
        df.drop(columns='Dividends', inplace=True)

    # Remove 'Stock Split' Column
    if 'Stock Split' in df.columns:
        df.drop(columns='Stock Split', inplace=True)
