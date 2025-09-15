import pandas as pd

def add_time_features(df: pd.DataFrame, target_col: str, datetime_col: str = None, n_lags: int = 0) -> pd.DataFrame:
    """
    Generate time-based features and lag features for energy demand forecasting.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the time series.
    target_col : str
        Name of the target column to create lag features from.
    datetime_col : str, optional
        Name of the datetime column. If None, the index is assumed to be a DatetimeIndex.
    n_lags : int, default 0
        Number of lag features to create from the target column.

    Returns
    -------
    pd.DataFrame
        Original DataFrame with added time-based features and optional lag features.
    """

    # Ensure datetime is available
    if datetime_col is not None:
        df[datetime_col] = pd.to_datetime(df[datetime_col])
        dt_index = df[datetime_col]
    else:
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame must have a DatetimeIndex or provide `datetime_col`.")
        dt_index = df.index

    ## Features

    df["Hour"] = dt_index.hour
    df["Day of week"] = dt_index.dayofweek
    df["is_weekend"] = df["Day of week"].isin([5, 6]).astype(int)
    df["Month"] = dt_index.month
    df["Year"] = dt_index.year

    # Season
    def season_from_month(month):
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "fall"

    df["Season"] = df["Month"].map(season_from_month)
    df = pd.get_dummies(df, columns=["Season"], drop_first=False)

    # Lag features
    if n_lags > 0:
        for lag in range(1, n_lags+1):
            df[f"{target_col}_lag_{lag}"] = df[target_col].shift(lag)
        df = df.dropna()  # drop rows with NaN caused by lags

    return df

