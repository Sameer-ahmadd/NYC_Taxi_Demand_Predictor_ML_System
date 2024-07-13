from datetime import datetime
from typing import Tuple

import pandas as pd


def train_test_split(
    df: pd.DataFrame,
    cutoff_date: datetime,
    target_column_name: str,
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """
    Splits the dataframe into training and testing datasets based on a cutoff date.
    """
    # Ensure pickup_hour column is of datetime type
    df['pickup_hour'] = pd.to_datetime(df['pickup_hour'])

    # Check if cutoff_date is timezone-aware and handle accordingly
    if cutoff_date.tzinfo is not None:
        # Convert pickup_hour to timezone-aware
        df['pickup_hour'] = df['pickup_hour'].dt.tz_localize(
            cutoff_date.tzinfo)
    else:
        # Remove timezone info from cutoff_date
        cutoff_date = cutoff_date.replace(tzinfo=None)

    train_data = df[df.pickup_hour < cutoff_date].reset_index(drop=True)
    test_data = df[df.pickup_hour >= cutoff_date].reset_index(drop=True)

    X_train = train_data.drop(columns=[target_column_name])
    y_train = train_data[target_column_name]
    X_test = test_data.drop(columns=[target_column_name])
    y_test = test_data[target_column_name]

    return X_train, y_train, X_test, y_test
