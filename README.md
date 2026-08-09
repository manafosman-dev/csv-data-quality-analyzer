# CSV Data Quality Analyzer

A Streamlit application that analyzes CSV files, identifies common data-quality problems, cleans the data, and produces a downloadable cleaned dataset.

## Features

- Upload and preview CSV files
- Calculate an overall data-quality score
- Detect missing values by column
- Detect duplicate rows
- Identify numeric outliers
- Fill missing numeric values using the median
- Fill missing text values using the mode
- Standardize column names
- Remove duplicate rows
- Compare original and cleaned quality scores
- Download the cleaned dataset
- Handle empty, malformed, and unsupported CSV files
- Automated tests for the cleaning pipeline

## Application Workflow

1. Upload a CSV file.
2. Review the dataset preview.
3. Inspect the quality score and detected issues.
4. Click **Clean Data**.
5. Compare the original and cleaned results.
6. Download the cleaned CSV file.

## Project Structure

```text
csv_data_quality_analyzer/
├── sample_data/
├── src/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── loader.py
│   ├── profiler.py
│   ├── scoring.py
│   └── validator.py
├── tests/
│   └── test_cleaner.py
├── app.py
├── pyproject.toml
├── requirements.txt
├── uv.lock
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- pandas
- Streamlit
- pytest
- uv

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd csv_data_quality_analyzer
```

Install the dependencies with `uv`:

```bash
uv sync
```

Alternatively, install from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Running the Tests

Run the complete test suite:

```bash
uv run python -m pytest -v
```

## Cleaning Rules

| Data-quality problem | Cleaning method |
|---|---|
| Missing numeric values | Replace with the column median |
| Missing text values | Replace with the column mode |
| Duplicate rows | Remove duplicated records |
| Untidy column names | Convert to lowercase snake case |
| Numeric outliers | Detect and report them |

Outliers are reported but not automatically removed because an extreme value may still be valid business data.

## Error Handling

The application displays readable messages for:

- Empty CSV files
- Malformed CSV files
- Unsupported file encodings
- Invalid uploaded data
- Unexpected processing errors

## Future Improvements

- User-selectable cleaning strategies
- Date-format validation
- Data-type correction
- Outlier-treatment options
- Downloadable quality reports
- Support for Excel files
- Interactive charts
- Processing of larger datasets

## Author

**Manaf Osman**

Data Analytics and Data Science Portfolio Project