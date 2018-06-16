import pymssql
import datetime
import time



server = 'localhost'  # 数据库服务器名称或IP
user = 'zjp'  # 用户名
password = '0419'  # 密码
database = 'airdatabase'  # 数据库名称
conn = pymssql.connect(server, user, password, database)#创建连接
cursor = conn.cursor()
if not cursor:
        raise Exception('数据库连接失败！')


# 判断数据库中各表是否存在，若不存在，则创建表
def judgetable():
    global cursor,conn
    cursor.execute('''IF not EXISTS(SELECT * FROM sysobjects WHERE name='TempRequest')
                        CREATE TABLE TempRequest (
                               roomnumber  varchar(50) NOT NULL,
                               nowDate  DATE,
                               target_temp FLOAT,  
                               durtime FLOAT,
                               ntime FLOAT )''')
    conn.commit()
    cursor.execute('''IF not EXISTS(SELECT * FROM sysobjects WHERE name='SpeedRequest')
                      CREATE TABLE SpeedRequest (
                               roomnumber  varchar(50) NOT NULL,
                               nowDate  DATE,
                               speed_type FLOAT,  
                               durtime FLOAT,
                               ntime FLOAT )''')
    conn.commit()
    cursor.execute('''IF not EXISTS(SELECT * FROM sysobjects WHERE name= 'OpenRequest')
                      CREATE TABLE OpenRequest (
                                   roomnumber  varchar(50) NOT NULL,
                                   openstate INTEGER,
                                   nowDate  DATE,
                                   nowTime  TIME)''')
    conn.commit()
    cursor.execute('''IF not EXISTS(SELECT * FROM sysobjects WHERE name='report')
                      CREATE TABLE report (
                                   roomnumber  varchar(50) NOT NULL,
                                   nowDate  DATE,
                                   nowTime  TIME ,
                                   code_type INTEGER ,  
                                   temp FLOAT,
                                   target_temp FLOAT,
                                   speed INTEGER,
                                   Energy FLOAT,
                                   Cost FLOAT)''')
    conn.commit()
    cursor.execute(''' IF not EXISTS(SELECT * FROM sysobjects WHERE name='Statistic')
    	                CREATE TABLE Statistic (
                                   nowDate  DATE,
                                   roomnumber  varchar(50),
                                   temp_times  INTEGER,
                                   work_times INTEGER,  
                                   report_num INTEGER)''')
    conn.commit()
starttime = time.time()#程序开始时间（全局变量）
# 插入温度请求表插入数据（房间号,当前日期,目标温度,持续时间,当前时间）注：插入的目标温度为改变前的,每次有调温或关机请求时插入
def insertTempRequest(roomnumber,target_temp):
    global cursor, conn
    cursor.execute("select max(ntime) from TempRequest where roomnumber='%s'" % roomnumber)
    row = cursor.fetchone()
    if row[0]:
        StartTime = row[0]#获取上个目标温度的开始时间
    else:
        StartTime = starttime
    ntime = time.time()#获取当前时间
    durtime = ntime - StartTime#计算上个目标温度的持续时间
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前日期
    cursor.execute("insert into TempRequest values('%s','%s',%f,%f,%f)" % (roomnumber,nowDate,target_temp, durtime,ntime))
    conn.commit()

# 风速请求表插入数据（房间号,当前日期,目标风速,持续时间,当前时间）注：插入的目标风速为改变前的,每次有调风或关机请求时插入
def insertSpeedRequest(roomnumber,speed_type):
    global cursor, conn
    cursor.execute("select max(ntime) from SpeedRequest where roomnumber='%s'"% roomnumber)
    row = cursor.fetchone()
    if row[0]:
        StartTime = row[0]  # 获取上个目标温度的开始时间
    else:
        StartTime = starttime
    ntime = time.time()  # 获取当前时间
    durtime = ntime - StartTime  # 计算上个目标温度的持续时间
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前日期
    cursor.execute("insert into SpeedRequest values('%s','%s',%f,%f,%f)"% (roomnumber,nowDate,speed_type, durtime,ntime))
    conn.commit()

# 开关机请求表插入数据（房间号,开关状态,当前时间）
def insertOpenRequest(roomnumber,openstate):
    global cursor, conn
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')
    cursor.execute("insert into OpenRequest values('%s',%d,'%s','%s')"% (roomnumber,openstate,nowDate,nowTime))
    conn.commit()

# 详单请求表插入数据（房间号，当前日期，当前时间，请求类型，当前温度，目标温度，当前风速，能量，费用）
def insertReport(roomnumber,code_type,temp,target_temp,speed,Energy,Cost):
    global cursor, conn
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    nowTime = datetime.datetime.now().strftime('%H:%M:%S')
    cursor.execute("insert into report values('%s','%s','%s',%f,%f,%f,%f,%f,%f)"% (roomnumber,nowDate,nowTime,code_type,temp,target_temp,speed,Energy,Cost))
    conn.commit()
# 打印详单
def printReport(roomnumber):
    global cursor, conn
    cursor.execute("select * from report where roomnumber=%s",roomnumber)
    data=cursor.fetchall()
    print("房间号\t日期\t时间\t请求类型\t当前温度\t目标温度\t当前风速\t能量\t费用")
    for row in data:
        print("%s\t%s\t%s\t%d\t%.1f\t%.1f\t%d\t%f\t%.2f"%(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8]))
    return data#返回详单数据
# 打印账单
def printCost(roomnumber):
    global cursor, conn
    cursor.execute("select roomnumber,Cost from report where roomnumber='%s'"% roomnumber)
    data = cursor.fetchall()
    print("房间号\t费用")
    for row in data:
        print("%s\t%.2f"%(row[0], row[1]))

    return data#返回账单数据

# 统计表插入数据（房间号,达到目标温度次数，调度次数，详单数）
def updateStatistics_temp_times(roomnumber,date):#插入达到目标温度次数
    global cursor, conn
    cursor.execute(''' if exists( select roomnumber from Statistic where roomnumber='%s' and nowDate='%s')
                        update Statistic set temp_times=temp_times+1 where roomnumber='%s'
                    else
                        insert into Statistic values('%s','%s',1,0,0)
                   ''' % (roomnumber,date,roomnumber,date,roomnumber))
    conn.commit()
def updateStatistics_work_times(roomnumber,date):#插入调度次数
    global cursor, conn
    cursor.execute(''' if exists( select roomnumber from Statistic where roomnumber='%s' and nowDate='%s')
                        update Statistic set work_times=work_times+1 where roomnumber='%s'
                    else
                        insert into Statistic values('%s','%s',0,1,0)
                   ''' % (roomnumber,date,roomnumber,date,roomnumber))
    conn.commit()
def updateStatistics_report_num(roomnumber,date):#插入详单数
    global cursor, conn
    cursor.execute(''' if exists( select roomnumber from Statistic where roomnumber='%s' and nowDate='%s')
                        update Statistic set report_num=report_num+1 where roomnumber='%s'
                    else
                        insert into Statistic values('%s','%s',0,0,1)
                   ''' % (roomnumber,date,roomnumber,date,roomnumber))
    conn.commit()

#从开关机请求表 温度请求表和风速请求表获取使用空调次数，最常用温度，最常用风速的函数
def Obtain(roomnumber):
    global cursor, conn
    cursor.execute("select count(openstate) from OpenRequest where openstate = 1 and roomnumber='%s'"% roomnumber)
    row = cursor.fetchone()
    opentimes = row[0]
    cursor.execute("select target_temp,max(durtime) from TempRequest where roomnumber='%s'"% roomnumber)
    row = cursor.fetchone()
    target_temp = row[0]
    cursor.execute("select speed_type,max(durtime) from SpeedRequest where roomnumber='%s'"% roomnumber)
    row = cursor.fetchone()
    speed_type = row[0]
    return opentimes,target_temp,speed_type

# 查询日报表
def printDailyReport(date):
    global cursor, conn
    cursor.execute('''select E.roomnumber,open_num,B.target_temp,C.speed_type,D.temp_times,D.work_times,D.report_num,E.fee
                      from (select roomnumber,count(openstate) as open_num from OpenRequest where openstate=1 and nowDate='%s' group by roomnumber) as A,
                      (select a.roomnumber,target_temp
	                  from (select roomnumber,max(durtime) as m_d from TempRequest where nowDate='%s' group by roomnumber)as a,TempRequest
	                  where a.roomnumber=TempRequest.roomnumber and a.m_d=TempRequest.durtime) as B,
                      (select a.roomnumber,speed_type
	                  from (select roomnumber,max(durtime) as m_d from SpeedRequest where nowDate='%s' group by roomnumber)as a,SpeedRequest
	                  where a.roomnumber=SpeedRequest.roomnumber and a.m_d=SpeedRequest.durtime) as C,
                      (select * from Statistic where nowDate='%s') as D,
	                  (select roomnumber,max(Cost) as fee from report where nowDate='%s' group by roomnumber) as E
                      where A.roomnumber=B.roomnumber and A.roomnumber=C.roomnumber and A.roomnumber=D.roomnumber and A.roomnumber=E.roomnumber
                  '''% (date,date,date,date,date))
    data=cursor.fetchall()
    print("房间号\t开关次数\t常用目标温度\t常用风速\t达到目标温度次数\t被调度次数\t详单数\t总费用")
    for row in data:
        print("%s\t%d\t\t\t%.2f\t\t\t%d\t\t\t%d\t\t\t\t\t%d\t\t\t%d\t\t%.2f" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    return data#返回报表数据

# 关闭连接
def closeConnection():
    global conn
    conn.close()