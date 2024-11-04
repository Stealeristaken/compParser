# CompParser

A Python utility class for data processing and text cleaning, designed to streamline common data manipulation tasks in data science workflows and Kaggle competitions.

## Features

- Memory optimization for pandas DataFrames
- Text cleaning and preprocessing
- Colored console output
- Object serialization and deserialization
- Support for multiple data types and formats

## Requirements

The following Python libraries are required:

- polars
- pandas
- numpy
- emoji
- ftfy
- stopwords
- colorama
- dill

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/CompParser.git
```

2. Navigate to the project directory:

```bash
cd CompParser
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from compParser import compParser

# Initialize the parser
parser = compParser()

# Example usage for memory optimization
df = pd.DataFrame(...)  # Your DataFrame
optimized_df = parser.reduce_mem_usage(df)

# Example usage for text cleaning
cleaned_text = parser.clean_text("Your text here", language="english")
```

### Available Methods

#### Memory Optimization

```python
# Reduce memory usage of a pandas DataFrame
df_optimized = parser.reduce_mem_usage(df, float16_as32=True)
```

#### Text Cleaning

```python
# Clean and preprocess text
cleaned_text = parser.clean_text(
    text="Your text with emojis 😊 and @mentions",
    language="english"
)
```

#### Object Serialization

```python
# Save an object to file
parser.pickleDump(your_object, "path/to/save.pkl")

# Load an object from file
loaded_object = parser.pickleLoad("path/to/save.pkl")
```

#### Colored Console Output

```python
# Print colored text to console
parser.PrintColor("Warning message", color=Fore.RED)
```

## Features in Detail

### Memory Optimization

The `reduce_mem_usage` method optimizes DataFrame memory usage by:

- Downcasting numerical columns to appropriate dtypes
- Supporting both integer and float type optimization
- Providing memory usage statistics before and after optimization

### Text Cleaning

The `clean_text` method performs the following operations:

- Emoji conversion to text
- Unicode fixing
- HTML tag removal
- URL removal
- @mention removal
- Single character removal
- Number removal
- Stopword removal (multiple languages supported)
- Whitespace trimming

### Object Serialization

- Supports saving and loading Python objects using dill
- Protocol 4 compatibility for better performance
- Binary file handling for efficient storage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
