# Data Driven Workflow with AWS S3 Buckets
Automated tests framework to ensure a Data Driven Workflow scenario using [Pytest](https://docs.pytest.org/en/7.2.x/)

## Data Driven Workflow - Definition
The application is a data driven workflow that works like this at a high level
Data files are submitting into an AWS S3 bucket
Processing is automatically initiated which will produce 2 outputs in serial order
Catalog Output is produced first
Product Output is produced only if the catalog output is successfully produced
The end user can successfully download the catalog and product files from the system

## Prerequisites

* Install [Docker](https://docs.docker.com/get-docker/) according to your OS

* Clone this repo `git clone https://github.com/LerryAlexander/data-driven-s3-aws.git` 
* Go to the root folder: `cd data-driven-s3-aws/`

## Usage

```
docker-compose up
```

## Report

Open the html report generated at: `./reports/report.hmtl`

## Test Cases

The following are the different test cases considered in the testing framework:

* Test case to verify that the data file is successfully uploaded to the AWS S3 bucket.
* Test case to verify that the system can handle multiple files being uploaded simultaneously.
* Test case to verify that the system generates a catalog output after processing the data file.
* Test case to verify that the system generates a product output only if the catalog output is successfully produced.
* Test case to verify that the end-user can download the catalog and product files from the system.
* Test case to verify that the system can handle failures during processing.
* Test case to verify that the whole process is completed within 3 minutes.
* Test case to verify that the data files are successfully deleted from AWS S3 bucket.

Other test cases that can be considered for automation:

* Test case to verify that the system can handle large files.
* Test case to verify that the system can handle a high volume of requests.
