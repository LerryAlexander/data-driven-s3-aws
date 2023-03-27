# Data Driven Workflow
Automated tests framework to ensure a Data Driven Workflow scenario using [Pytes](https://docs.pytest.org/en/7.2.x/)

## Prerequisites

* Install [Docker](https://docs.docker.com/get-docker/) according to your OS

* Clone this repo `git clone`

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

Other test cases that can be considered for automation:

* Test case to verify that the system can handle large files.
* Test case to verify that the system can handle a high volume of requests.
