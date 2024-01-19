#!/usr/bin/python3
"""takes in the name of a state as an argument
and lists all cities of that state"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE %s "
                "ORDER BY cities.id", (sys.argv[4],))
    query_rows = cur.fetchall()

    cities = ""
    for row in query_rows:
        cities += row[0] + ", "
    print(cities[0: -2:])
    cur.close()
    conn.close()
