#Code này mình cũng có tham khảo của bạn Minh Sơn
import insertUtil as ut
import psycopg2


#Tạo kết nối với RDS PostgreSQL và thêm dữ liệu vào
conn = psycopg2.connect(database='covid19_postgres', user='postgres', password='12345678', host='database-postgresql.cmfe1d9zikny.us-east-1.rds.amazonaws.com', port='5432')
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')