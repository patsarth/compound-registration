#!/usr/bin/env python3

from aws_cdk import core
import os
from data_lake_setup.datalake_batch_stack import DatalakeBatchStack
from data_lake_setup.datalake_batch_job_def_stack import DatalakeBatchJobStack
from data_lake_setup.datalake_secret_manager_stack import DatalakeSecretManagerStack
from data_lake_setup.datalake_lambda_stack import DatalakeLambdaStack
from data_lake_setup.datalake_glue_stack import DatalakeGlueStack

""" Define your account id to make import vpc work """
env_cn = core.Environment(account=os.environ.get("AccountId"), region=os.environ.get("AwsRegion"))

""" Initialising environment variables and creating a dictionary to pass"""
config_dict = {}
config_dict['env_var'] = os.environ.get("EnvironVarLower")
config_dict['vpc_id'] = os.environ.get("VpcId")
config_dict['SubnetIds'] = os.environ.get("SubnetIds")
config_dict['AvailabilityZones'] = os.environ.get("AvailabilityZones")
config_dict['workflow_ecr_repo'] = os.environ.get("WorkflowEcrRepository")
config_dict['datalake_bucket_name'] = "gfb-datalake-" + config_dict['env_var'].lower()
config_dict['datalake_db_name'] = "gfb_datalake_db"
config_dict['workflow_comp_reg_image_version'] = os.environ.get("WorkflowCompRegImage")
config_dict['comp_reg_secret_name'] = os.environ.get("CompRegSecretName")
config_dict['comp_reg_host_name'] = os.environ.get("CompRegHostName")
config_dict['comp_reg_port'] = os.environ.get("CompRegPort")
config_dict['comp_reg_db_name'] = os.environ.get("CompRegDBName")
config_dict['comp_reg_user_name'] = os.environ.get("CompRegUserName")
config_dict['comp_reg_password'] = os.environ.get("CompRegPassword")
config_dict['workflow_assay_image_version'] = os.environ.get("WorkflowAssayETLImageVersion")
config_dict['idbs_base_url'] = os.environ.get('BaseIDBSUrl')
config_dict['idbs_secret_name'] = os.environ.get('IDBSSecretName')

""" Start execution of deployment """
app = core.App()
DatalakeBatchStack(app, "datalake-batch-stack", config_dict, env=env_cn)
DatalakeBatchJobStack(app, "datalake-batch-job-stack", config_dict, env=env_cn)
DatalakeSecretManagerStack(app, "datalake-secret-manager-stack", config_dict, env=env_cn)
DatalakeLambdaStack(app, "datalake-lambda-stack", config_dict, env=env_cn)
DatalakeGlueStack(app, "datalake-glue-stack", config_dict, env=env_cn)

app.synth()
