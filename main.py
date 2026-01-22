from app.scrapper.kbb import kbb_worker
import time
import os
import psutil

def print_ram_usage(note=""):
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 ** 2)
    print(f"[RAM] {note} {mem_mb:.2f} MB")


if __name__ == "__main__":
    start_time = time.time()
    print_ram_usage("Start")

    df = kbb_worker()
    # Win
    # print_ram_usage("After scraping")
    # os.makedirs("Car-Recommendation-System/data/raw", exist_ok=True)

    # Mac
    DATA_DIR = "data/raw"
    os.makedirs(DATA_DIR, exist_ok=True)


    if df.empty:
        print("⚠️ No data scraped. CSV not saved.")
    else:
        # df.to_csv("Car-Recommendation-System/data/raw/car_data.csv", index=False) # Win
        df.to_csv(f"{DATA_DIR}/car_data.csv", index=False) # Mac
        print("✅ Data saved to Car-Recommendation-System/data/raw/car_data.csv")

    elapsed = time.time() - start_time
    print_ram_usage("After saving CSV")
    print(f"Process time: {elapsed:.2f} seconds")


#WINDOWS:.venv\Scripts\Activate
#