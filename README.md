# xtivia
# Python script
In the python script, boto3 is imported to use the python SDK for AWS

The os module is imported to allow passing of environment variables at runtime into the docker container

Environment variables being passed at runtime are:
- The S3 source bucket
- The S3 destination bucket
- The minimum size threshold for a transfer from the source to the destination S3 bucket respectively

#Anatomy of the Docker file
The docker file starts with the python:3.9-slim as the base layer

An /app directory is set as the working directory

The python script is copied into the working directory

pip is used to install boto3 and awscli

#Running the application in docker
To run the application in docker, the following steps are taken:

- Build image `docker build -t <image_name> .`

- AWS credentials will need to be passed to docker either by passing it at runtime or by mounting the credential file from the base system. 

- To run the container from the image using AWS credentials passed in as environment variables, run the following command: 

```
docker run \
-e AWS_ACCESS_KEY_ID=" " \
-e AWS_SECRET_ACCESS_KEY=" " \
-e SRC_BUCKET_NAME=" " \
-e DST_BUCKET_NAME=" " \
-e MIN_OBJECT_SIZE=" " <image_name>
```
- To run the container from the image using AWS credentials mounted as a read only file (ro)

```
docker run -v $HOME/.aws/credentials:/root/.aws/credentials:ro \
-e AWS_PROFILE=" " \
-e SRC_BUCKET_NAME=" " \
-e DST_BUCKET_NAME=" " \
-e MIN_OBJECT_SIZE=" " <image_name>

```





