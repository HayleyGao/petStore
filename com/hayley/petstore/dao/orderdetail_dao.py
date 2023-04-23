from com.hayley.petstore.dao.base_dao import BaseDao


class OrderDetailDao(BaseDao):
    def __init__(self):
        super().__init__()

    def create(self,orderdetail):

        if orderdetail is not None:
            orderid=orderdetail['orderid']
            productid=orderdetail['productid']
            quantity=orderdetail['quantity']
            unitcost=orderdetail['unitcost']
        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                sql = "insert into orderdetails(orderid,productid,quantity,unitcost) values(%s,%s,%s,%s)"%(orderid,productid,quantity,unitcost)
                affectedcount = cursor.execute(sql)
                print('成功插入{0}条数据'.format(affectedcount))
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.close()


