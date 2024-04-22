# Credit card fraud detection app

## Project description 

The credit card fraud detection app is a web application that predicts whether a data is legit or fraud  based on features such as time, glucose level, V1-V28, and Amount. 
The app utilizes a machine learning model trained on a dataset containing information about customer,  The dataset contains transactions made by credit cards in September 2013 by European cardholders. 
This dataset presents transactions that occurred in two days, where we have 492 frauds out of 284,807 transactions. 
The dataset is highly unbalanced, the positive class (frauds) account for 0.172% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. 
Unfortunately, due to confidentiality issues, we cannot provide the original features and more background information about the data.
Features V1, V2, … V28 are the principal components obtained with PCA, the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. 
The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-sensitive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

### Features
The features used in the dataset are as follows:
1. Time in seconds
2. V1
3. V2
4. .......
5. V8
6. Amount

#### Model Used
The machine learning model used in the app is Convolutional Neural Network (CNN).
This model is chosen for its ability to handle tabular data and provide accurate predictions for binary classification tasks like credit card fraud prediction.

##### Model Evaluation

The model's performance is evaluated using an accuracy score, which measures the percentage of correctly predicted outcomes out of all predictions made on the test dataset.

###### How to Run

1. Clone the repository
   ``




