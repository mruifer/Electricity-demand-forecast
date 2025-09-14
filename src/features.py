import pandas as pd

def add_time_features(df: pd.DataFrame, datetime_col: str = None) -> pd.DataFrame:
    """
    Generate time-based features for energy demand forecasting.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the time series.
    datetime_col : str, optional
        Name of the datetime column. If None, the index is assumed to be a DatetimeIndex.

    Returns
    -------
    pd.DataFrame
        Original DataFrame with added time-based features.
    """

    # Ensure datetime is available
    if datetime_col is not None:
        df[datetime_col] = pd.to_datetime(df[datetime_col])
        dt_index = df[datetime_col]
    else:
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("DataFrame must have a DatetimeIndex or provide `datetime_col`.")
        dt_index = df.index

    # Hour of the day (0–23)
    df["Hour"] = dt_index.hour

    # Day of the week (0=Monday, 6=Sunday)
    df["Day of week"] = dt_index.dayofweek

    # Is weekend (1 if Saturday/Sunday)
    df["is_weekend"] = df["Day of week"].isin([5, 6]).astype(int)

    # Month (1–12)
    df["Month"] = dt_index.month

    # Season (categorical: winter, spring, summer, fall)
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

    # Convert to numerical value each season
    df = pd.get_dummies(df, columns=["Season"], drop_first=True)

    return df
