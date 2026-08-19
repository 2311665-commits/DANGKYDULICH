import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-912f4c2-dlu-48d3.d.aivencloud.com",

        port=21119,

        user="avnadmin",

        password="AVNS_kloBO8x2u3t9NxItETL",

        database="company1",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
