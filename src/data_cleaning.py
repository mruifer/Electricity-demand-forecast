import matplotlib.pyplot as plt
import pandas as pd

def fill_values(df: pd.DataFrame, fill_method: str = "interpolate")-> pd.DataFrame:
    """
    Fill missing values in a time series DataFrame using a specified method.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the time series with potential missing values (NaN).
    fill_method : str, default "interpolate"
        Method to fill missing values. Options:
        - "ffill": forward fill using the last valid observation.
        - "bfill": backward fill using the next valid observation.
        - "interpolate": linear interpolation based on time index.
        - None: leave NaN values as is.

    Returns
    -------
    pd.DataFrame
        DataFrame with missing values filled according to the chosen method.
    """

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
    dup_error : bool, default False
        If we consider that duplicated values are errors (True) to eliminate them or not (False) to use their mean value.
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

    # Fix diferent frequency (with the mean value of all the values inside a period), 
    # adds mising timestamps (empty values) and duplicates if they are not errors
    df = df.resample(freq).mean()

    # Fill empty values
    df=fill_values(df, fill_method)

    return df

def fix_anomalies(df: pd.DataFrame, column: str, show: bool=True)-> pd.DataFrame:
    """
    Detect and fix anomalies in a time series by clipping extreme values.

    This function replaces extreme low and high values with the 1st and 99th percentile values,
    respectively, effectively removing outliers. It also gives the possibility to plot a 24-hour 
    rolling mean to help visualize the impact of anomaly removal.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the time series.
    column:
        Name of the numeric column to check for anomalies.
    show : bool, default True
        To show or not the fixed Dataframe.

    Returns
    -------
    pd.DataFrame
        DataFrame with anomalies clipped to the 1st and 99th percentiles.
    """
    
    # Fix anomalies
    q_low = df[column].quantile(0.01)
    q_high = df[column].quantile(0.99)
    df[column] = df[column].clip(lower=q_low, upper=q_high)

    if show==True:
        # Plot the resulting data
        plt.figure(figsize=(15,5))
        plt.plot(df[column].rolling(24).mean())
        plt.title("Rolling mean (24h) to detect anomalies")
        plt.show()

    return df