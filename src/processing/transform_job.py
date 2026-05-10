import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1770337882855 = glueContext.create_dynamic_frame.from_catalog(database="windfarm", table_name="my_pipeline_engdados_project", transformation_ctx="AWSGlueDataCatalog_node1770337882855")

# Script generated for node Data Lake
EvaluateDataQuality().process_rows(frame=AWSGlueDataCatalog_node1770337882855, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1770337773083", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
DataLake_node1770338092841 = glueContext.write_dynamic_frame.from_options(frame=AWSGlueDataCatalog_node1770337882855, connection_type="s3", format="glueparquet", connection_options={"path": "s3://my-pipeline-engdados-project/data-lake/processed/glue/", "partitionKeys": ["type"]}, format_options={"compression": "snappy"}, transformation_ctx="DataLake_node1770338092841")

job.commit()