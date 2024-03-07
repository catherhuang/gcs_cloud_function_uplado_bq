import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
import io

def process_csv(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    bucket_name = file['bucket']
    blob_name = file['name']

    # Download the CSV file
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    csv_string = blob.download_as_string().decode('utf-8')

    # Process the CSV
    df = pd.read_csv(io.StringIO(csv_string))
    df.columns = df.columns.str.lower()  # Convert column names to lowercase

    # Load into BigQuery
    client = bigquery.Client()
    dataset_id = 'cat-looker-core-argolis-demo.cat_demo_data'
    table_id = blob_name.replace('.csv', '')  # Table name from file name

    job_config = bigquery.LoadJobConfig(autodetect=True)  # Auto-detect schema
    job = client.load_table_from_dataframe(df, dataset_id + '.' + table_id, job_config=job_config)
    job.result()  # Wait for the job to complete
