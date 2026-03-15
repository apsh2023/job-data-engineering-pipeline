import requests
import pandas as pd
import os

def run_scraper():
    # 1. Use the API instead of HTML (much more reliable)
    url = "https://remoteok.com/api"
    
    # Remote OK requires a specific User-Agent even for the API
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
    }

    print(f"Connecting to {url}...")
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if we got blocked (403) or not found (404)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return

        # The API returns a list of dictionaries (JSON)
        json_data = response.json()
        
        # The first item in the Remote OK API is usually legal/meta info, so we skip it
        jobs = json_data[1:] 

        data = []
        for job in jobs:
            data.append({
                "job_id": job.get("id"),
                "date": job.get("date"),
                "company": job.get("company"),
                "position": job.get("position"),
                "salary": f"{job.get('salary_min', 0)} - {job.get('salary_max', 0)}",
                "tags": ", ".join(job.get("tags", [])),
                "url": job.get("url")
            })

        # 2. Convert to DataFrame
        df = pd.DataFrame(data)

        # 3. Handle Directory & CSV Cleanup
        output_dir = "../data/raw"
        file_path = f"{output_dir}/jobs.csv"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # OVERWRITE: 'w' mode (default in to_csv) ensures the file is wiped and refreshed
        if not df.empty:
            df.to_csv(file_path, index=False, encoding='utf-8')
            print("-" * 30)
            print(f"Success! Found {len(data)} jobs.")
            print(f"Cleaned and updated: {file_path}")
        else:
            print("No jobs found in the API response.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_scraper()