#Code này mình cũng có tham khảo của bạn Minh Sơn
import insertUtil as ut
import MySQLdb


#Tạo kết nối với RDS Aurora MySQL và thêm dữ liệu vào
conn = MySQLdb.connect(host='database-aurora.cluster-cmfe1d9zikny.us-east-1.rds.amazonaws.com', user='admin', passwd='12345678', db='covid19_aurora', port=3306)
print('Open DB successfully')
ut.insert(conn)
ut.select(conn)
conn.close()
print('Successfully')


