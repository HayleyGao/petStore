from com.hayley.petstore.dao.base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        """
        查询所有商品信息
        :return:
        """
        products = []
        try:
            with  self.conn.cursor() as cursor:
                # 通过继承后的连接对象，获取游标
                sql = "select * from products"
                cursor.execute(sql)

                result_set = cursor.fetchall()  # 获取结果集

                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['cname'] = row[1]
                    product['ename'] = row[2]
                    product['image'] = row[3]
                    product['descn'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['category'] = row[7]
                    products.append(product)

        except Exception as e:
            raise e
        finally:
            self.close()

        return products

    def findbycat(self, catname):
        """
        按照商品类别名称查找商品
        :param catname:
        :return:
        """
        products = []
        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                sql = "select * from products where category=%s" % catname
                cursor.execute(sql)

                result_set = cursor.fetchall()  # 获取结果集

                for row in result_set:
                    product = {}
                    product['productid'] = row[0]
                    product['cname'] = row[1]
                    product['ename'] = row[2]
                    product['image'] = row[3]
                    product['descn'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['category'] = row[7]
                    products.append(product)
            # with代码块结束，关闭游标cursor。
        except Exception as e:
            raise e
        finally:
            self.close()

        return products

    def findbyid(self, productid):
        """
        按照商品id查找商品
        :param catname:
        :return:
        """
        product=None

        try:
            # 通过继承后的连接对象，获取游标
            with self.conn.cursor() as cursor:  # cursor = self.conn.cursor()
                sql = "select * from products where productid='%s'" % productid
                cursor.execute(sql)

                row = cursor.fetchone()  # 获取结果集

                if row is not None:
                    product = {}
                    product['productid'] = row[0]
                    product['cname'] = row[1]
                    product['ename'] = row[2]
                    product['image'] = row[3]
                    product['descn'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['category'] = row[7]

            # with代码块结束，关闭游标cursor。
        except Exception as e:
            raise e
        finally:
            self.close()

        return product
