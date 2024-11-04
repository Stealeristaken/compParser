# CompParser

This project is a Python library designed for simple data mining and data cleaning processes in Kaggle competitions. It includes basic functions such as data manipulation and memory optimization.

## Features

- Parse computational data files
- Extract and analyze data
- Generate summary reports

## Requirements

- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CompParser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd CompParser
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:

```bash
python compParser.py [options]
```

### Options

- `-i`, `--input`: Specify the input file
- `-o`, `--output`: Specify the output file
- `-h`, `--help`: Show the help message

## Example

```bash
python compParser.py -i data/input.txt -o results/output.txt
```

## Sample Code

```python
from compParser import compParser

parser = compParser()
df = parser.reduce_mem_usage(df)
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
