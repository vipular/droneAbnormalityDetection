# SAD3 Dataset (Synthetic Abnormality Detection Dataset for Drones)

## Dataset Description

### Folder Description:

The given dataset consists of two folders namely _"Data_CSV"_ & _"Data_BAG"_. The former consists of CSV files containing the preprocessed data, and the latter consists of bag files containing unprocessed data. In both the abovementioned folders, the data files are divided into two folders, namely _"Normal"_ & _"Abnormal"_. The difference between the two sets is that all files in the _"Abnormal"_ contain some kind of abnormality in them. 

The abnormal CSV files available in this given datasets are of two kinds; namely _"combined_csv"_ and _"raw_csv"_, wherein the former contains the ground truth (denoted by _"state"_) and the preprocessed data variables in a single CSV file whereas the latter contains both of these mentioned parameters in separate CSV files. A subset of the generated abnromal files have their ground truth available, and therefore are available in the _"combined_csv"_ format.



### CSV Files Description:

The CSV files under the _"Normal"_ folder and the _"raw_csv"_ subfolder in the "Abnormal" folder have their values arranged in the following format (in SI Units):


| Index | Time | Image Similarity Score | Orientation(X) | Orientation(Y) | Orientation(Z) | Orientation(W) | Angular Velocity(X) | Angular Velocity(Y) | Angular Velocity(Z) | Linear Acceleration(X) | Linear Acceleration(Y) | Linear Acceleration(Z) | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

The CSV files under the _"combined_csv"_ subfolder in the _"Abnormal"_ folder have their values arranged in the following format (in SI units):


| Index | Time | Image Similarity Score | Orientation(X) | Orientation(Y) | Orientation(Z) | Orientation(W) | Angular Velocity(X) | Angular Velocity(Y) | Angular Velocity(Z) | Linear Acceleration(X) | Linear Acceleration(Y) | Linear Acceleration(Z) | Ground Truth | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |



**_Note:_** The values under the Ground Truth column are binary. A value of one implies normal behaviour at the given time instant whereas a value of 0 implies abnormal behaviour.



Total Number of datapoints in Normal Training Files = 5576

| File number | Time Steps | Duration |
|---|---|---|
|/Data_CSV/Normal/file1.csv  |951|95.027 s|
|/Data_CSV/Normal/file2.csv  |495|56.533 s|
|/Data_CSV/Normal/file3.csv |589|58.87 s|
|/Data_CSV/Normal/file4.csv |769|80.535 s|
|/Data_CSV/Normal/file5.csv |454|45.24 s|
|/Data_CSV/Normal/file6.csv  |857|89.948 s|
|/Data_CSV/Normal/file7.csv  |858|90.983 s|
|/Data_CSV/Normal/file8.csv  |603|59.48 s|
|Total Time steps/Duration | 5576|576.606 s|

Total Number of datapoints in Abnormal Training Files = 1564
| File number | Time Steps | Duration |
|---|---|---|
|/Data_CSV/Abnormal/file1.csv   |423|45.135 s|
|/Data_CSV/Abnormal/file2.csv |435|44.023 s|
|/Data_CSV/Abnormal/file3.csv |259|25.975 s|
|/Data_CSV/Abnormal/file4.csv  |447|44.598 s|
| Total Time steps/Duration | 1564 |159.731 s|

Total Number of datapoints in Testing Files (Containing both normal and abnormal points) = 3027
| File number | Time Steps | Duration |
|---|---|---|
|/Data_CSV/Abnormal/file5.csv |1008|105.8 s|
|/Data_CSV/Abnormal/file6.csv  |753|79.049 s|
|/Data_CSV/Abnormal/file7.csv  |773|79.289 s|
|/Data_CSV/Abnormal/file8.csv|493|58.963 s|
|Total Time Steps/Duration | 3027 |323.101 s|




