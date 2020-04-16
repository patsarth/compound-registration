import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="data_lake_setup",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "data_lake_setup"},
    packages=setuptools.find_packages(where="data_lake_setup"),

    install_requires=[
        "aws-cdk.core==1.32.0",
        "aws-cdk.aws_s3",
        "aws-cdk.aws_ec2",
        "aws-cdk.aws_batch",
        "aws-cdk.aws_iam",
        "aws-cdk.aws_glue",
        "aws-cdk.aws_lambda",
        "aws-cdk.aws_athena",
        "aws-cdk.aws_ecs",
        "aws-cdk.aws_ecr",
        "aws_cdk.aws_secretsmanager",
        "aws_cdk.aws_lambda",
        "aws-cdk.aws_s3_notifications",
        "aws_cdk.aws_lambda_event_sources"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
