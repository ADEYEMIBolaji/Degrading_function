# Data Degradation Function

This repository contains a Python function for degrading a dataset by introducing random noise and modifications to various data types. The purpose of this function is to simulate real-world data scenarios, where data imperfections and uncertainties are common.

## Usage

### Installation

To use the data degradation function, you'll need to have Python installed. You can clone this repository or simply download the `data_degradation.py` file.

### Importing the Function

To import the data degradation function, include the following line in your Python script:

```python
from data_degradation import degrade_dataset
```

### Function Signature

The function `degrade_dataset` accepts the following parameters:

```python
degrade_dataset(df, noise_factor=0.1, categorical_replace_prob=0.1, numerical_replace_prob=0.1, string_replace_prob=0.1)
```

- `df`: Pandas DataFrame - The input dataset to be degraded.
- `noise_factor`: float (default: 0.1) - The factor controlling the level of noise added to numerical columns.
- `categorical_replace_prob`: float (default: 0.1) - The probability of replacing values in categorical columns.
- `numerical_replace_prob`: float (default: 0.1) - The probability of replacing values in numerical columns.
- `string_replace_prob`: float (default: 0.1) - The probability of replacing values in string columns.

### Example Usage

Here's an example of how to use the data degradation function:

```python
import pandas as pd
from data_degradation import degrade_dataset

# Assuming you have a DataFrame named 'original_df'
# ...

noise_factor = 0.1
categorical_replace_prob = 0.1
numerical_replace_prob = 0.1
string_replace_prob = 0.1

degraded_df = degrade_dataset(original_df, noise_factor, categorical_replace_prob, numerical_replace_prob, string_replace_prob)

print("Original DataFrame:")
print(original_df)

print("\nDegraded DataFrame:")
print(degraded_df)
```

### Customization

You can customize the degradation parameters (`noise_factor`, `categorical_replace_prob`, `numerical_replace_prob`, and `string_replace_prob`) based on the level of degradation you want to introduce to your dataset. It is essential to fine-tune these parameters to suit your specific use case and desired level of data degradation.

## Contributing

If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request. Your contributions are welcome and will be appreciated.

## License



## Acknowledgments

The data degradation function is based on concepts and techniques commonly used to simulate real-world data variations in machine learning and data science experiments. Special thanks to the open-source community for providing valuable resources and inspiration.
