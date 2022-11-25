# Construction of a Machine_Learning_Workflow_AWS pipeline using AWS Lambda and step Functions

workflow automates the whole process of preprocessing, prediction using an API and returns results in S3 Bucket

## WorkFlow compentents:
 
### Lambda Functions:
  
  - Seriliziing Lambda #1: takes an input Json to the workflow where it contains the S3 bucket name that has the data and extracts the images from that Bucket
  
  - Classification Lambda #2: takes the output of lambda #1 and passes the images to the deployed Model EndPoint and returns Predictions in Json
  
  - Filter Lambda #3: takes the output of lambda #3 and filters the images that had a score below a threshold
  
### Step Function:

  - step function oragnizes the flow of execution of the three lambda functions in order
  
  - The Three Lambda's are wrraped in a map function to map the 3 process to multiple images in a parallel
  
### Backend API:

  - an image classifier is deployed with AWS to an endpoint on ml.m4.xlarge instance
  
 ### S3:
 
  - every data to be used for the model are uploaded and stored in an S3 Bucket
  
 ### Model Monitor:
 
  - data capture is enables when deploying the API to capture jsonl files about operations done through the API and saved in S3
  
  Check the starter notebook for implemntation detalis
