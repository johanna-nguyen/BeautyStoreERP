import mysql.connector


class Model:
    def __init__(self,
                 host = 'localhost',
                 database = 'store_management_db',
                 username='root',
                 password = '61184khanhnguyen'):
        self.host = host
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        self.connect_db()


    def connect_db(self):
        try:
            self.connection = mysql.connector.connect( host=self.host,
                user=self.username,
                password=self.password,
                database=self.database)
            #print("Kết nối thành công")
        except Exception as e:
            print("Lỗi kết nối: ",e)

    def query(self, sql):
        """Thực thi câu lệnh SQL không có tham số"""
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        return result

    def query_params(self, sql, params):
        """Thực thi câu lệnh SQL có tham số"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, params)

            # Nếu là câu lệnh SELECT, trả về kết quả
            if sql.strip().upper().startswith("SELECT"):
                # Lấy tất cả các dòng kết quả
                results = cursor.fetchall()
                cursor.close()
                return results

            # Nếu không phải SELECT, commit và trả về True
            self.connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(f"Lỗi khi thực thi câu lệnh SQL: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Đóng kết nối")