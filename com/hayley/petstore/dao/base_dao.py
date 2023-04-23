import pymysql
import configparser


class BaseDao:
    def __init__(self):
        """
        连接数据库
        """
        # 获取配置文件中的内容
        self.config = configparser.ConfigParser()
        self.config.read(r'/Users/hayleygao/PycharmProjects/petStore/config.ini', encoding='utf-8')
        # 连接数据库，读取数据库内容
        host = self.config['db']['host']
        port = self.config['db']['port']
        user = self.config['db']['user']
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

        self.conn = pymysql.connect(host=host, port=int(port), user=user, password=password, database=database,
                               charset=charset)

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        self.conn.close()
