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



Number of datapoints in Normal Files

| File number | Total Time Steps |
