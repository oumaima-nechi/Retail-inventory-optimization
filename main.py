from tests.test_db_connection import test_database_connection
from tests.test_etl import run_pipeline
from tests.test_etl_dwh import run_dwh_process

choice=input("Choose data format ['csv','sql','json']: ")
if choice=="sql":
    connection = test_database_connection()
    if connection:  # Only proceed if the connection is successful
        print("Database connection successful. Running ETL pipeline...")

        # Run the ETL pipeline
        run_pipeline(choice)  # Call the function directly
        run_dwh_process()  # Call the function
    else:
        print("Database connection failed. ETL pipeline will not run.")
    # Close connection if it was successfully opened
    if connection:
        connection.close()
        print("Connection closed.")
elif choice=="csv" or choice=="json":
    run_pipeline(choice)
    run_dwh_process()  

else: 
    print("not available choice, try again")
