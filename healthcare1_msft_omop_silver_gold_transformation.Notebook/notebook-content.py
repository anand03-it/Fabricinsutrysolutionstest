# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "fc6cd5e2-54b9-4460-b083-03313c124cf1",
# META       "default_lakehouse_name": "healthcare1_msft_gold_omop",
# META       "default_lakehouse_workspace_id": "786aa193-6403-46c3-b7ef-eef483bd939c"
# META     },
# META     "environment": {
# META       "environmentId": "4a844314-cccc-8f44-44da-f3ba63869132",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ##### WARNING
# The following notebook is intended to be read only. Please do not modify the contents of this notebook.


# CELL ********************

%run healthcare1_msft_config_notebook

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

%run healthcare1_msft_config_notebook {"enable_spark_setup" : true, "enable_packages_mount" : false}

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# PARAMETERS CELL ********************

inline_params = "{}"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark",
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

# Invoke the OMOPIngestionService to transform and load tables into target lakehouse
from microsoft.fabric.hls.hds.services.omop_ingestion_service import OMOPIngestionService
import json

# convert inline params into dictionary
inline_params_dict = json.loads(inline_params)

# Invoke the OMOPIngestionService to transform and load tables into target lakehouse
omop_ingestion_service = OMOPIngestionService(
        spark=spark,
        workspace_name=workspace_name,
        solution_name=solution_name,
        admin_lakehouse_name=administration_database_name,
        inline_params=inline_params_dict,
        one_lake_endpoint=one_lake_endpoint
        )
omop_ingestion_service.run()

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }

# CELL ********************

mssparkutils.fs.unmount(packages_mount_name)

# METADATA ********************

# META {
# META   "frozen": false,
# META   "editable": false
# META }
