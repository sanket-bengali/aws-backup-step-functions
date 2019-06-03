import boto3
import datetime
import time

def create_db_snapshot(event, context):

    db_instance_id = event['db_instance_id']
    region_name = event['region_name']

    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%Y-%m-%d-%H-%M-%S")
    db_instance_snapshot_id = db_instance_id + "-" + time_string
    print("DB instance snapshot id : " + db_instance_snapshot_id)

    client = boto3.client('rds', region_name=region_name)
    client.create_db_snapshot(DBInstanceIdentifier=db_instance_id, DBSnapshotIdentifier=db_instance_snapshot_id)

    return db_instance_snapshot_id
