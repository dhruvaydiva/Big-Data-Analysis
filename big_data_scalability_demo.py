import os, glob, numpy as np, pandas as pd

def run_pandas(data_path="./data"):
    files = glob.glob(f"{data_path}/events/*/*.parquet")
    if not files:
        print("No Parquet files found. Generate data with the notebook first.")
        return
    df = pd.concat([pd.read_parquet(f) for f in files], ignore_index=True)
    df["revenue"] = np.where(df["event_type"].eq("purchase"), df["price"]*df["quantity"], 0.0)
    df["date"] = pd.to_datetime(df["event_time"]).dt.date
    print("Daily revenue sample:\\n", df.groupby("date")["revenue"].sum().head())

if __name__ == "__main__":
    run_pandas()