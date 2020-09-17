# import sqlite3 as s
#
# # MySQL Connection 연결
# conn = s.connect('')
#
# # Connection 으로부터 Cursor 생성
# c = conn.cursor()
#
# # SQL문 실행
# sql = "select * from Query_1"
# c.execute(sql)
#
# # Data Fetch
# rows = c.fetchall()
# print(rows)     # 전체 rows
# # print(rows[0])
#
# # Connection 닫기
# conn.close()