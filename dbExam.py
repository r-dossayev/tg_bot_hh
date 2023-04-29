import psycopg2
def bubbleSort(arr):
    n = len(arr)
    for f in range(n - 1):
        for g in range(0, n - f - 1):
            if arr[g] > arr[g + 1]:
                arr[g], arr[g + 1] = arr[g + 1], arr[g]


con = psycopg2.connect(
    database="pythonDb",
    user="postgres",
    password="postgre",
    host="127.0.0.1",
    port="5432"
)

cur = con.cursor()


cur.execute("SELECT name,id FROM CATEGORIES")
ret = cur.fetchall()


def myCatVacs(i):
    cur.execute(f'SELECT * FROM VACANCIES WHERE cat_id={i}')
    myee = cur.fetchall()
    return myee


ccc1 = myCatVacs(1)
ccc2 = myCatVacs(2)
ccc3 = myCatVacs(3)
ccc4 = myCatVacs(4)
ccc5 = myCatVacs(5)
ccc6 = myCatVacs(6)
ccc7 = myCatVacs(7)

arr = [ccc1, ccc2, ccc3, ccc4, ccc5, ccc6, ccc7]


def myVacJobs(j):
    cur.execute(f'SELECT * FROM JOBS WHERE vac_id={j}')
    myJobs = cur.fetchall()
    return myJobs


cur.execute("SELECT vac_id FROM JOBS INNER JOIN VACANCIES ON jobs.vac_id=vacancies.id GROUP BY vac_id;")
xxx2 = cur.fetchall()
# print(xxx2)
mynewxxx2 = []
for d in xxx2:
    mynewxxx2.append(d[0])
bubbleSort(mynewxxx2)
# print(mynewxxx2)
arr2 = []
for i in mynewxxx2:
    arr2.append(myVacJobs(i))
# print(arr2)
# print(arr2[0])
# print(arr2)


# for y in myCatVacs(1):
#     print(y[2])
# for row in ret:
#     print("NAME =", row[0])
#     print("surname =", row[1], )
#     print("date =", row[2], )


def newJob(myCity, myName, myUser_url, myVac_id, myUserId):
    sql = "INSERT INTO jobs ( city,name, user_url, vac_id, user_id) VALUES ( %s, %s, %s,%s,%s)"
    val = (myCity, myName, myUser_url, myVac_id, myUserId)
    cur.execute(sql, val)
    con.commit()


def myJobs(myUser):
    sql = "SELECT city, name FROM jobs WHERE user_id = %s"
    val = (myUser,)
    cur.execute(sql, val)
    q =cur.fetchall()
    return q


con.commit()
# con.close()


