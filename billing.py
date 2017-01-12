#!/usr/bin/env python

import datetime
import json
import sys

from boto.ec2 import cloudwatch


def get_billing(profile):

    conn = cloudwatch.CloudWatchConnection(profile_name=profile)

    data = conn.get_metric_statistics(
        namespace="AWS/Billing",
        dimensions={'Currency': "USD"},
        start_time=datetime.datetime.now() - datetime.timedelta(hours=12),
        end_time=datetime.datetime.now(),
        period=60,
        statistics=["Sum"],
        metric_name="EstimatedCharges"
    )

    return max(data, key=lambda x: x['Timestamp'])


def format_billing(data):
    ret = {}
    ret['billing'] = data['Sum']
    ret['timestamp'] = data['Timestamp'].strftime('%s')

    return json.dumps(ret)


def main():
    args = get_args()
    profile = args.get('profile')

    print(format_billing(get_billing(profile)))


def get_args():
    argvs = sys.argv
    # argc = len(argvs)
    ret = {}

    ret['profile'] = argvs[1]

    return ret


if __name__ == "__main__":
    exit(main())
