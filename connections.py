import MySQLdb


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="surajkamble",
                           db="CloudP1")
    c = conn.cursor()

    return c, conn