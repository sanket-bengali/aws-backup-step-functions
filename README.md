# AWS services backup using Step functions

This sample solution includes 2 [State machines](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-lambda-state-machine.html) to take backup of AWS services :

1. Single AWS service backup workflow

![Alt text](https://github.com/sanket-bengali/aws-backup-step-functions/blob/master/images/Neo4j%20backup%20WF.png?raw=True "Custom Volume backup workflow")

Execution of this state machine requires below input parameters (by Lambda functions) :

```
{
  "host_ip": "x.y.z.w",
  "username": "ubuntu",
  "s3-key-bucket": "my_key_bucket",
  "key-path": "keys/my_key.pem",
  "s3-script-bucket": "my_script_bucket",
  "pre-script-path": "step_functions/scripts/pre-script.sh",
  "volume_id": "vol-xxxxx",
  "region_name": "aws_region",
  "post-script-path": "step_functions/scripts/post-script.sh",
}
```

2. Two AWS services backup (in parallel) workflow

![Alt text](https://github.com/sanket-bengali/aws-backup-step-functions/blob/master/images/Myapp%20backup%20WF.png?raw=True "Custom volume and DB backup workflow")

Execution of this state machine requires below input parameters (by Lambda functions) :

```
{
  "host_ip": "x.y.z.w",
  "username": "ubuntu",
  "s3-key-bucket": "my_key_bucket",
  "key-path": "keys/my_key.pem",
  "s3-script-bucket": "my_script_bucket",
  "pre-script-path": "step_functions/scripts/pre-script.sh",
  "volume_id": "vol-xxxxx",
  "db_instance_id": "my_db_instance_id",
  "region_name": "aws_region",
  "post-script-path": "step_functions/scripts/post-script.sh",
}
```

The state machines execute below [AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) for each step :

### NOTE : These lambda functions can be packaged with a deployment package using Python's virtualenv as mentioned [here](https://aws.amazon.com/blogs/compute/scheduling-ssh-jobs-using-aws-lambda/)

1. pre_script_handler.py

   Performs below operations :
   
   a. Download the EC2 instance SSH key and pre-script from the given location in S3 bucket
   
   b. Copy the script to a temp directory in the EC2 instance, change its permissions and execute
   
2. volume_snapshot_launch_handler.py

   Launch Volume snapshot for given <volume_id> and <region_name>, and store the snapshot id in <volume_snapshot_id>.
   
3. volume_snapshot_status_check_handler.py

   Get volume snapshot status for the <volume_snapshot_id>.
   
4. db_snapshot_launch_handler.py

   Launch DB snapshot for the given <db_instance_id> and <region_name>, and store the snapshot id in <db_instance_snapshot_id> (db_instance_id + "%Y-%m-%d-%H-%M-%S").
   
5. db_snapshot_status_check_handler.py

   Get the DB snapshot status for the <db_instance_snapshot_id>.
   
6. post_script_handler.py

   Performs below operations :
   
   a. Download the EC2 instance SSH key and post-script from the given location in S3 bucket
   
   b. Copy the script to a temp directory in the EC2 instance, change its permissions and execute

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.
