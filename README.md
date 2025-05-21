# Retail-inventory-optimization

> Advanced analytics platform for retail inventory management and sales optimization

## 🚀 Features

* **Data Integration**: Processes and integrates data from various sources, including sales records, inventory logs, and promotional data.
* **Interactive Dashboards**: Visualizes key metrics such as sales trends, inventory levels, and promotional performance using Tableau.
* **Predictive Analytics**: Utilizes demand forecasting to maintain optimal inventory levels and prevent overstocking or stockouts.
* **Scalable Data Warehouse**: Implements a star schema for efficient data storage and analysis.
* **ETL Pipeline**: Automates data extraction, transformation, and loading for seamless processing.

## 📂 Project Structure

1. **Data Collection**:
   * **Sources**: Retail sales data from Kaggle, merged with additional store and product details.
   * **Formats**: CSV, JSON, and SQL.

2. **ETL Process**:
   * **Extract**: Reads raw data into pandas DataFrames.
   * **Transform**: Cleanses data by handling missing values, removing duplicates, and standardizing formats.
   * **Load**: Stores the processed data in a SQL-based data warehouse.

3. **Data Modeling**:
   * **Star Schema**: Includes fact tables for sales and dimension tables for stores, products, and time.
   * **Data Marts**: Optimized subsets for targeted business analysis.

4. **Data Analysis**:
   * **Store Performance**: Analyzes sales trends and inventory levels.
   * **Product Performance**: Identifies top-performing products and evaluates promotional impacts.
   * **Demand Analysis**: Forecasts demand and analyzes city-based trends.

## 💻 Code Overview

* **Main Program**: Orchestrates the BI pipeline.
* **ETL Scripts**:
   * **Extract**: Reads raw data.
   * **Transform**: Cleans and prepares data.
   * **Load**: Inserts data into the data warehouse.
* **Testing**: Validates ETL processes and database connections.

## 📊 Tools & Technologies

* **Languages**: Python (pandas, SQLAlchemy)
* **Database**: MySQL
* **BI Tool**: Tableau
* **IDE**: Visual Studio Code

## 📈 Results

The BI dashboard provides insights into:
* **Store Efficiency**: Highlights top-performing stores and their contribution to total sales.
* **Product Trends**: Identifies high-demand categories and evaluates promotions.
* **Future Planning**: Uses predictive analytics to forecast demand and guide inventory management.

## 🔧 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/username/retail-bi-system.git
cd retail-bi-system

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure database connection
cp config.example.py config.py
# Edit config.py with your database credentials

# Run the ETL pipeline
python src/main.py
```

