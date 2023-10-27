# end-to-end-mlops-data-science-project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

## Setting tracking URL
MLFLOW_TRACKING_URI=https://dagshub.com/ny-essien/end-to-end-mlops-data-science-project.mlflow \
MLFLOW_TRACKING_USERNAME=ny-essien \
MLFLOW_TRACKING_PASSWORD=db1ed1d23f1438e860b575a6fe58f9856d40eadb \
python script.py

Run this to export as env variables

``` bash

export MLFLOW_TRACKING_URI= https://dagshub.com/ny-essien/end-to-end-mlops-data-science-project.mlflow 
export MLFLOW_TRACKING_USERNAME=ny-essien 
export MLFLOW_TRACKING_PASSWORD=db1ed1d23f1438e860b575a6fe58f9856d40eadb 


```