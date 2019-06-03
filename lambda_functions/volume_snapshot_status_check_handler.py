import boto3

def get_volume_snapshot_state(event, context):

    volume_snapshot_id = event['volume_snapshot_id']
    region_name = event['region_name']

    ec2_client = boto3.client('ec2', region_name=region_name)
    snapshot_details = ec2_client.describe_snapshots(SnapshotIds=[volume_snapshot_id])
    print("Snapshot details :\n" + str(snapshot_details))
 
    volume_snapshot_state = snapshot_details['Snapshots'][0]['State']
    print("Snapshot state : " + volume_snapshot_state)

    return volume_snapshot_state
