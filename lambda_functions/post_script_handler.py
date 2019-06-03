import boto3
import paramiko

def execute_post_script(event, context):

    s3_key_bucket = event['s3-key-bucket']
    key_path = event['key-path']

    s3_client = boto3.client('s3')
    #Download private key file from secure S3 bucket

    key_path_splitted = key_path.split("/")
    key_name = key_path_splitted[-1]
    s3_client.download_file(s3_key_bucket, key_path, '/tmp/' + key_name)

    k = paramiko.RSAKey.from_private_key_file('/tmp/' + key_name)
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    host = event['host_ip']
    username = event['username']

    print("Connecting to " + host)
    c.connect( hostname = host, username = username, pkey = k )
    print("Connected to " + host)

    s3_script_bucket = event['s3-script-bucket']
    post_script_path = event['post-script-path']
    post_script_path_splitted = post_script_path.split("/")
    post_script_name = post_script_path_splitted[-1]
  
    post_script_execution_path = "/home/" + username + "/" + post_script_name
    commands = [
        "aws s3 cp s3://" + s3_script_bucket + "/" + post_script_path + " " + post_script_execution_path,
        "chmod 700 " + post_script_execution_path,
        "sh " + post_script_execution_path
        ]

    for command in commands:
        print("Executing {}".format(command))
        stdin , stdout, stderr = c.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        print("Stdout :\n" + output)
        print("Stderr :\n" + error)

    return "Post-script execution completed."
