import pymysql
import traceback
import datetime
import random

class DBHelper:
    def __init__(self):
        # 链接数据库
        try:
            # charset 默认是 latin1, 查询到中文会是？？
            # charset='utf8mb4' 避免有表情时插入错误
            self.__db = pymysql.connect(
                host='192.168.100.21',
                port = 3306,
                user='root',
                password='unimob@12254ns',
                database='achievement',
                charset='utf8mb4')
            self.__cur = self.__db.cursor()
        except pymysql.Error:
            print('链接数据库失败：', traceback.print_exc())

    def insert(self, table, myDict):
        # 答案中存在表情会出错
        # 答案中存在双引号会出错，sql语句会发生歧义
        # 插入一条数据
        try:
            cols = ','.join(myDict.keys())
            values = ','.join(
                map(lambda x: '"' + str(x) + '"', myDict.values()))
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, cols, values)
            self.__cur.execute(sql)
            self.__db.commit()
        except pymysql.Error:
            print('插入失败：', traceback.print_exc())
            # 发生错误时回滚
            # DML 语句，执行完之后，处理的数据，都会放在回滚段中（除了 SELECT 语句），
            # 等待用户进行提交（COMMIT）或者回滚 （ROLLBACK），当用户执行 COMMIT / ROLLBACK后，
            # 放在回滚段中的数据就会被删除。
            self.__db.rollback()

    def query(self, sql):
        try:
            self.__cur.execute(sql)
            result = self.__cur.fetchall()
            self.__db.commit()
            if result:
                return result
            else:
                return None

        except pymysql.Error:
            print("数据库-查询异常", traceback.print_exc())

    '''
    查询数据库中是否已经存在record
    '''

    def check_exist(self, table, my_dict):
        try:
            if not len(my_dict):
                return
            values = ' AND '.join(
                map(lambda x: str(x) + '= "' + str(my_dict[x]) + '"', my_dict.keys()))
            print(values)
            sql = 'SELECT COUNT(*) FROM %s WHERE 1=1 AND %s' % (table, values)
            print(sql)
            self.__cur.execute(sql)
            results = self.__cur.fetchall()
            if results[0][0] > 0:
                return True
            else:
                return False

        except pymysql.Error:
            print('查询失败！', traceback.print_exc())
            return False

    def close(self):
        self.__cur.close()
        self.__db.close()


dbhelpser = DBHelper()
# my_dict = {'ip': '61.155.164.108:3128'}
types = {
    '10':'试题新增',
    '11':'试题删除',
    '12':'试题更新',
    '20':'套卷新增',
    '21':'套卷删除',
    '22':'套卷更新'
}

for n in range(200):
    operate_type = list(types.keys())[n % 6]
    my_dict = {
        'id': n + 201,
        'biz_status': 1,
        'gmt_create': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'gmt_modify': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'operator': '张萌',
        'operate_type': operate_type,
        'operate_type_name': types[operate_type],
        'operate_target_id': random.randint(1, 200),
        'content':'helloworld',
        'modifier_content':'2019年是很重要的军事周年'
    }
    dbhelpser.insert('operate_record', my_dict)
# print(dbhelpser.check_exist('t_meizitu_proxy_ip', my_dict))