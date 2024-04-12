#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
