Big Data Scalability Demo
-------------------------

Files included:
- big_data_scalability_demo.ipynb  : Jupyter notebook with Dask/PySpark/pandas pipelines (scalable)
- big_data_scalability_demo.py    : Lightweight pandas fallback script
- requirements.txt                : Recommended Python packages to install
- README.md                       : This file

How to use:
1. Install dependencies:
   pip install -r requirements.txt
2. Generate synthetic data using the notebook (it includes partitioned parquet writer).
3. Run notebook cells with Dask / Spark configured, or run the python script for pandas fallback.

Notes:
- The notebook contains cells to generate partitioned Parquet data, then shows equivalent
  Dask and PySpark pipelines for aggregations (daily revenue, top products, device mix, etc.).