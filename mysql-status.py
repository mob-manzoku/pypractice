#!/usr/bin/env python3
import os
import argparse
import json
import MySQLdb
import MySQLdb.cursors


def create_sql():

    sql = "show session variables"
    return sql


def main():
    args = define_parsers()
    conn = create_db_connection(args.host, args.user, args.passwd, args.db, args.charset)

    sql = create_sql()

    cursor = conn.cursor()
    cursor.execute(sql)

    for row in cursor.fetchall():
        print(json.dumps(row))

    cursor.close()


def create_db_connection(host, user, password, db, charset="latin1"):

    connector = MySQLdb.connect(
        host=host,
        user=user,
        passwd=password,
        db=db,
        cursorclass=MySQLdb.cursors.DictCursor,
        charset=charset
    )

    return connector


def define_parsers():
    parser = argparse.ArgumentParser(description='MySQL Snippet',
                                     add_help=False)
    parser.add_argument('--help', action='help', help='help')

    parser.add_argument('-u', '--user', type=str, default=os.environ.get('USER', "root"),
                        help='MySQL user. default: USER enviroment value')

    parser.add_argument('-h', '--host', type=str, default=os.environ.get('MYSQL_HOST', "localhost"),
                        help='MySQL host. default: MYSQL_HOST enviroment value')

    parser.add_argument('-p', '--passwd', type=str, default=os.environ.get('MYSQL_PWD', ""),
                        help='MySQL password. default: MYSQL_PWD enviroment value')

    parser.add_argument('--db', type=str, default="INFORMATION_SCHEMA",
                        help='MySQL Database name. default: INFORMATION_SCHEMA')

    parser.add_argument('--charset', type=str, default="utf8mb4",
                        help='set_client_charset. default: utf8mb4')

    parser.add_argument('--dry-run', dest='dry_run', action='store_true',
                        help='Dry run')
    parser.set_defaults(dry_run=False)

    return parser.parse_args()


if __name__ == "__main__":
    main()
