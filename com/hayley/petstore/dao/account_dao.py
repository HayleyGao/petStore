from com.hayley.petstore.dao.base_dao import BaseDao


class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findbyid(self, userid):
        account = None
        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                print(userid,'---------------')
                sql = "select * from accounts where id='%s'" % userid  # %s 占位符
                # sql = "select * from accounts where id='a-001'"  # %s 占位符
                cursor.execute(sql)

                row = cursor.fetchone()  # 获取结果集

                if row is not None:
                    account = {}
                    account['id'] = row[0]
                    account['password'] = row[1]
                    account['email'] = row[2]
                    account['name'] = row[3]
                    account['address'] = row[4]
                    account['city'] = row[5]
                    account['country'] = row[6]
                    account['phone'] = row[7]
            # with代码块结束，关闭游标cursor。
        except Exception as e:
            raise e
            print(e)
        finally:
            self.close()

        return account
