from com.hayley.petstore.dao.base_dao import BaseDao


class OrderDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        orders = []
        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                sql = "select * from orders"
                cursor.execute(sql)

                orders_set = cursor.fetchall()  # 获取结果集

                for row in orders_set:
                    order = {}
                    order['orderid'] = row[0]
                    order['userid'] = row[1]
                    order['order_datetime'] = row[2]
                    order['status'] = row[3]
                    order['amount'] = row[4]
                    orders.append(order)
            # with代码块结束，关闭游标cursor。
        except Exception as e:
            raise e
            print(e)
        finally:
            self.close()
        return orders

    def create(self, order):
        """
        创建订单，插入到数据库
        :param order:
        :return:
        """
        if order is not None:
            orderid = order['orderid']
            userid=order['userid']
            order_datetime=order['order_datetime']
            status=order['status']
            amount=order['amount']
        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                sql = "insert into orders(orderid,userid,order_datetime,status,amount) values(%s,%s,%s,%s,%s)" % (
                    orderid,userid,order_datetime,status,amount)
                affectedcount=cursor.execute(sql)
                print('成功插入{0}条数据'.format(affectedcount))
                # with代码块结束，关闭游标cursor。
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.close()
