import pandas as pd

def fill_values(df: pd.DataFrame, fill_method: str = "interpolate")-> pd.DataFrame:
    if fill_method == "ffill":
        df = df.fillna(method="ffill")
    elif fill_method == "bfill":
        df = df.fillna(method="bfill")
    elif fill_method == "interpolate":
        df = df.interpolate(method="time")
    elif fill_method is None:
        pass  # Leave NaN 
    else:
        raise ValueError(f"Unknown fill_method: {fill_method}")
    return df

def fix_time_irregularities(df: pd.DataFrame, datetime_col: str = None, freq: str = "h",dup_error: bool = False, fill_method: str = "interpolate") -> pd.DataFrame:
    """
    Fix common temporal irregularities in a time series DataFrame:
    - Ensure a uniform frequency (default hourly).
    - Remove duplicate timestamps (aggregate if necessary).
    - Fill missing timestamps with NaN, then impute missing values.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the time series.
    datetime_col : str, optional
        Name of the datetime column. If None, the index is assumed to be a DatetimeIndex.
    freq : str, default "h"
        Target frequency (e.g., "h" for hourly, "d" for daily).
    agg : str, default "mean"
        Aggregation method to apply if duplicates exist (e.g., "mean", "sum", "first").
    fill_method : str, default "ffill"
        Method to fill missing values ("ffill", "bfill", "interpolate", or None).

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with a uniform DatetimeIndex.
    """

    # Ensure datetime index
    if datetime_col is not None:
        df[datetime_col] = pd.to_datetime(df[datetime_col])
        df = df.set_index(datetime_col)
    elif not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("DataFrame must have a DatetimeIndex or provide `datetime_col`.")

    # Sort by datetime
    df = df.sort_index()

    # Handle duplicates if they are errors
    if dup_error==True:
        df = df[~df.index.duplicated(keep="first")]     # Eliminates second duplicate

    # Fix diferent frequency (with the mean value of all the values inside a period), adds mising timestamps (empty values) and duplicates if they are not errors
    df = df.resample(freq).mean()

    # Fill empty values
    df=fill_values(df, fill_method)

    return df