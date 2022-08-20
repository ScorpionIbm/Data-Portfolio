# Summary of the project
This is an ETL (Extract, transform and load) project aimed at helping sparkify load hte data available at hand about songs and logfiles into a database for further uses and data analsysis.

# How to run the Python scripts
The scripts are run from terminal.
## Create Table Script
The command used to run the script to create tables is:

    python3 create_tables.py
## ETL Script
The command used to run the script to create tables is:

    python3 etl.py
# Files in the repository
The repository consists of 6 files:
- sql_queries.py: contains SQL queries used in the ETL process, these are split in a separate file for better project organization and ease of use and editing
- create_tables.py: This script is responsible for initializing the database from scratch and using the sql_queries file to create the appropriate tables.
- etl.ipynb: This is a jupyter notebook outlining the main steps of the ETL process on sample files before loadin g the whole dataset.
- etl.py: The main ETL script, this applies the same ETL process outlined in the jupyter notebook and uses the SQL queries in sql_queries to insert the data extracted from the raw data files. 
- test.ipynb: the supplied basic tests and sanity checks for the basic checks on the ETL process.

There is also the data folder which contains all raw data files used for the ETL process.