import psycopg2

conn = psycopg2.connect(
     host = "switchback.proxy.rlwy.net",
     port = 26950,
     user = "postgres",
     password = "brjMXQCsQFglYObPGMKCQzKpisYAtDkA",
    database = "railway"
)

try:
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS STUDENT (
                id INT PRIMARY KEY,
                name VARCHAR(50),
                age INT
            )
            """)

            # Insert sample rows (use parameterized queries to avoid SQL injection)
            students = [
                (1, 'Alice', 21),
                (2, 'Bob', 22),
            ]
            cursor.executemany(
                "INSERT INTO STUDENT (id, name, age) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
                students
            )

            # Fetch and display rows
            cursor.execute("SELECT id, name, age FROM STUDENT ORDER BY id;")
            rows = cursor.fetchall()
            print("STUDENT rows:")
            for row in rows:
                print(row)
    print("connected successfully and inserted values")
except Exception as e:
    print("error:", e)
finally:
    if conn:
        conn.close()








