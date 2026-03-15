import pandas as pd
import os
from datetime import datetime

# --- CONFIGURATION ---
RAW_FILE = "./data/raw/jobs.csv"
CLEANED_FILE = "../data/processed/jobs_cleaned.csv"

def extract():
    """Reads the raw data from the Bronze layer."""
    print("📦 Step 1: Extracting raw data...")
    if not os.path.exists(RAW_FILE):
        raise FileNotFoundError(f"Missing raw data at {RAW_FILE}. Run your scraper first!")
    return pd.read_csv(RAW_FILE)

def transform(df):
    """Cleans and standardizes the data (Silver layer)."""
    print("🧪 Step 2: Transforming and cleaning data...")
    
    # 1. Deduplicate based on job_id
    initial_count = len(df)
    df = df.drop_duplicates(subset=['job_id'])
    print(f"   - Removed {initial_count - len(df)} duplicates.")

    # 2. Date Standardization
    # Converts 2026-03-03T... into 2026-03-03
    df['date'] = pd.to_datetime(df['date']).dt.date

    # 3. Salary Feature Engineering
    # Splitting "120000 - 180000" into two numeric columns
    salary_split = df['salary'].str.split(' - ', expand=True)
    df['min_salary'] = pd.to_numeric(salary_split[0], errors='coerce').fillna(0).astype(int)
    df['max_salary'] = pd.to_numeric(salary_split[1], errors='coerce').fillna(0).astype(int)
    
    # Calculate average salary for easier analysis later
    df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2

    # 4. Content Cleaning
    df['company'] = df['company'].str.strip().fillna('Unknown')
    df['position'] = df['position'].str.strip().fillna('Unknown')
    
    # Remove the old messy salary string
    df = df.drop(columns=['salary'])
    
    return df

def load(df):
    """Saves the cleaned data to the Silver layer."""
    print(f"💾 Step 3: Loading cleaned data to {CLEANED_FILE}...")
    output_dir = os.path.dirname(CLEANED_FILE)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    df.to_csv(CLEANED_FILE, index=False)
    print("✅ Pipeline run successful!")

# --- ORCHESTRATION ---
if __name__ == "__main__":
    try:
        raw_data = extract()
        clean_data = transform(raw_data)
        load(clean_data)
    except Exception as e:
        print(f"❌ Pipeline failed: {e}")