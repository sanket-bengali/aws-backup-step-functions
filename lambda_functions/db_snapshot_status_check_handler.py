import boto3

def get_db_instance_snapshot_status(event, context):

    db_instance_snapshot_id = event['db_instance_snapshot_id']
    region_name = event['region_name']

    client = boto3.client('rds', region_name=region_name)
    snapshot_details = client.describe_db_snapshots(DBSnapshotIdentifier=db_instance_snapshot_id)
    print("Snapshot details :\n" + str(snapshot_details))
 
    db_instance_snapshot_status = snapshot_details['DBSnapshots'][0]['Status']
    print("Snapshot status : " + db_instance_snapshot_status)

    return db_instance_snapshot_status
