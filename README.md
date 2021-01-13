# SAD3 Dataset (Synthetic Abnormality Detection Dataset for Drones)

## Dataset Description

### Folder Description:

The given dataset consists of two folders namely "Data_CSV" & "Data_BAG". The former consists of CSV files containing the preprocessed data, and the latter consists of bag files containing unprocessed data. In both the abovementioned folders, the data files are divided into two folders, namely "Normal" & "Abnormal". The difference between the two sets is that all files in the "Abnormal" contain some kind of abnormality in them. 

The abnormal CSV files available in this given datasets are of two kinds; namely "combined_csv" and "raw_csv", wherein the former contains the ground truth (denoted by "state") and the preprocessed data variables in a single CSV file whereas the latter contains both of these mentioned parameters in separate CSV files. A subset of the generated abnromal files have their ground truth available, and therefore are available in the "combined_csv" format.

### CSV Format Description:

The CSV files under the "Normal" folder and the "raw_csv" subfolder in the "Abnormal" folder have their values generated in the following format (in SI Units):


| Index | Time | Image Similarity Score | Orientation(X) | Orientation(Y) | Orientation(Z) | Orientation(W) | Angular Velocity(X) | Angular Velocity(Y) | Angular Velocity(Z) | Linear Acceleration(X) | Linear Acceleration(Y) | Linear Acceleration(Z) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | --- | ---- | --- | --- | --- | --- |
