import boto3

def create_volume_snapshot(event, context):

    volume_id = event['volume_id']
    region_name = event['region_name']

    ec2 = boto3.resource('ec2', region_name=region_name)
    volume = ec2.Volume(volume_id)
    snapshot = volume.create_snapshot()

    volume_snapshot_id = snapshot.id
    print("Snapshot id : " + volume_snapshot_id)
 
    return volume_snapshot_id
