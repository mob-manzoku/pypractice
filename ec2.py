#!/usr/bin/env python
import argparse
import botocore.session


def __main():
    args = define_parsers()
    session = botocore.session.get_session()
    client = session.create_client('ec2', region_name='ap-northeast-1')

    name_tag_filters = []
    if args.name is not None:
        name_tag_filters = [
            { 'Name': "tag:Name",
              'Values': [
                  args.name
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


def define_parsers():
    parser = argparse.ArgumentParser(description='EC2',
                                     add_help=False)
    parser.add_argument('--help', action='help', help='help')
    parser.add_argument('-n', '--num', type=int, default="0",
                        help='Ideal number')
    parser.add_argument('--name',type=str,
                        help='tag name')
    return parser.parse_args()


if __name__ == "__main__":
    exit(__main())
