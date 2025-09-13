import os
import pandas as pd

def load_single_file(file_path: str) -> pd.DataFrame:
    """
    Load a single CSV file with datetime parsing and set Datetime as index.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        DataFrame indexed by Datetime, sorted chronologically.
    """
    df = pd.read_csv(file_path, parse_dates=["Datetime"])
    df = df.sort_values("Datetime")
    df.set_index("Datetime", inplace=True)
    return df


def load_all_data(raw_dir: str = "../data/raw") -> dict:
    """
    Load all CSV files in the raw data directory.

    Parameters
    ----------
    raw_dir : str, optional
        Path to the raw data directory (default is ../data/raw).

    Returns
    -------
    dict
        Dictionary where keys are file names (without .csv) 
        and values are DataFrames indexed by Datetime.
    """
    dataframes = {}
    for file in os.listdir(raw_dir):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            path = os.path.join(raw_dir, file)
            dataframes[name] = load_single_file(path)
    return dataframes


def load_concatenated(raw_dir: str = "../data/raw") -> pd.DataFrame:
    """
    Load and concatenate all CSV files into a single DataFrame
    with an additional 'region' column.

    Parameters
    ----------
    raw_dir : str, optional
        Path to the raw data directory (default is ../data/raw).

    Returns
    -------
    pd.DataFrame
        Concatenated DataFrame with columns ['region', ...] 
        indexed by Datetime.
    """
    dfs = []
    for file in os.listdir(raw_dir):
        if file.endswith(".csv"):
            name = file.replace(".csv", "")
            path = os.path.join(raw_dir, file)
            df = load_single_file(path)
            df["region"] = name
            dfs.append(df)
    if dfs:
        return pd.concat(dfs)
    else:
        raise FileNotFoundError(f"No CSV files found in {raw_dir}")
