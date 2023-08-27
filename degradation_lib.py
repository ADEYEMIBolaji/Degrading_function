import pandas as pd
import random
import string

def add_random_noise(value, noise_factor=0.1):
    """Add random noise to a numerical value."""
    noise = random.uniform(-noise_factor, noise_factor)
    return value + noise

def replace_with_random_value(value, values_list):
    """Replace a value with a random value from the provided list."""
    return random.choice(values_list)

def replace_with_random_string(length=5):
    """Replace a string with a random string of given length."""
    return ''.join(random.choices(string.ascii_letters, k=length))

def add_random_future_date(value, max_days=365):
    """Add a random future date offset."""
    days_offset = random.uniform(0, max_days)
    return value + pd.Timedelta(days=days_offset)

def add_random_later_date(value, max_days=365):
    """Add a random later date offset."""
    days_offset = random.uniform(0, max_days)
    return value - pd.Timedelta(days=days_offset)

def degrade_dataset(df, noise_factor=0.1, categorical_replace_prob=0.1, numerical_replace_prob=0.1, string_replace_prob=0.1, date_replace_prob=0.1, exclude_columns=[]):
    """Randomly degrade a Pandas DataFrame with different techniques based on data types."""
    degraded_df = df.copy()

    for column in df.columns:
        if column in exclude_columns:
            continue  # Skip columns specified in the exclude_columns list

        if df[column].dtype in [int, float]:
            degraded_df[column] = df[column].apply(lambda x: add_random_noise(x, noise_factor))
        elif df[column].dtype == object:
            # Degrade categorical columns by randomly replacing values
            if random.random() < categorical_replace_prob:
                unique_values = df[column].unique()
                degraded_df[column] = df[column].apply(lambda x: replace_with_random_value(x, unique_values))
        elif df[column].dtype == bool:
            # Degrade boolean columns by flipping values
            degraded_df[column] = df[column].apply(lambda x: not x)
        elif df[column].dtype == pd.Timestamp:
            # Degrade date columns by adding random future and later date offsets
            if random.random() < date_replace_prob:
                degraded_df[column] = df[column].apply(lambda x: add_random_future_date(x))
            elif random.random() < date_replace_prob:
                degraded_df[column] = df[column].apply(lambda x: add_random_later_date(x))
        elif df[column].dtype == str:
            # Degrade string columns by replacing with random strings
            if random.random() < string_replace_prob:
                degraded_df[column] = df[column].apply(lambda x: replace_with_random_string())

    return degraded_df
