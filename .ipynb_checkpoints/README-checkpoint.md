# Repository for practice simple pipeline for wrangling and preprocessing data

## Autos data wrangling and preprocessing

The aim of this project is to create simple pipeline for data wrangling and preprocessing autos dataset. So, in the future when I work with this autos dataset again, the data wrangling and preprocessing process automatically follow this pipeline step or I can develop for the another purpose

## Process

Here below are the step of process to create pipeline for data wrangling and preprocessing autos dataset :

* Install package requirements for this project
* Read csv file into dataframe
* Rename some columns name into snake case type
* Change value type into datetime format for columns (ad_created, date_crawled, last_seen)
* Perform the cleaning data for column price and odometer, so the value from that column we can change into integer format
* Drop the column seller and offer_typ because the unique value of that column are inbalance
* Drop the column num_of_pictures because all the value is 0
* Drop the column name and postal_code because that columns less useful for our purpose
* Handle outliers for price columns
* Handle missing value. For column that has value type an object, fill missing value with mode. For column that has value type a numeric, fill missing value with median
* Perform the reset index
* perform the normalization process for columns with numeric data type, except for the price column because we will make it the target column in the future
* Perform the encoding process for columns of categorical data type
* Save the data that has been cleaned and pre-processed into csv format

## Review and Feedback

I really appreciate for the review and feedback. Let's connect with my [linkedIn](https://www.linkedin.com/in/rickisubagya/) account.