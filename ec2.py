#!/usr/bin/env python
import botocore.session

## TODO 引数にする
NAMETAG="api-prod"

def __main():
    session = botocore.session.get_session()
    client = session.create_client('ec2', region_name='ap-northeast-1')

    name_tag_filters = [
        { 'Name': "tag:Name",
          'Values': [
              NAMETAG
          ]
        }
    ]

    instances = []

    for reservation in client.describe_instances(Filters=name_tag_filters)['Reservations']:
        for instance in reservation['Instances']:

            for tag in instance['Tags']:
                if tag['Key'] == "Name":
                    tag_name = tag['Value']
                    break

            i = {
                'InstanceId': instance['InstanceId'],
                'LaunchTime': instance['LaunchTime'],
                'TagName': tag_name
            }
            instances.append(i)

    for i in sorted(instances, key=lambda x:x['LaunchTime']):
        print(i['LaunchTime'], i['InstanceId'], i['TagName'])


if __name__ == "__main__":
    exit(__main())
