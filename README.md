# Simple ETL Pipeline

A beginner-friendly Python script for basic data processing tasks that supports both CSV files and API data sources.

## 📋 Features

- **Extract**: Load data from CSV files or APIs
- **Transform**: Remove duplicates and handle missing values  
- **Load**: Export cleaned data to CSV format
- **Beginner-friendly**: Simple, commented code perfect for learning

## 🚀 Usage

### Option 1: CSV File Input
```python
# Change the file path to your CSV file
file_path = "/path/to/your/data.csv"
python simple_etl_pipeline.py
```

### Option 2: API Input  
Uncomment the API section in the code:
```python
# Uncomment these lines:
# import requests
# api_url = "https://api.example.com/data"
# response = requests.get(api_url)
# data = pd.DataFrame(response.json())
```

## 📁 Files

- `simple_etl_pipeline.py` - Main ETL script
- `cleaned_data.csv` - Output file (generated after running)

## 🛠️ Requirements

```bash
pip install pandas
pip install requests  # Only if using API option
```

## 🎯 Perfect For

- Learning ETL concepts
- Data cleaning tasks
- Quick data processing
- Beginner Python projects

## 👨‍💻 Author

Pedro Siqueira - Data enthusiast learning ETL pipelines

---

*Simple, clean, and educational - exactly what beginners need!*
