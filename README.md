# gcs_cloud_function_uplado_bq
step by step guide on how to use cloud function to detect uploaded csv in Google cloud function to bigquery  

in the cloud shell, enter the following command ```pip install google-cloud-functions google-cloud-storage google-cloud-bigquery pandas pyarrow```

before creating the cloud function: 
* set up a storage bucket
* create a dataset in BQ where the updated csv will land 

1. create new cloud function in google cloud console
   * environment: 2nd gen
   * function name: function-upload-csv-gcs-bq
   * region: region_of_your_storage_bucket
   * trigger type: cloud storage
   * event type: google.cloud.storage.object.v1.finalized
   * bucket: name_of_storage_bucket 
2. click next and update the code for main.py and requirements.txt 
   * runtime: python 3.9
   * entry point: process_csv
3. deploy


to trigger, upload csv to the storage bucket, and see the table populate in BQ 
