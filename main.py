import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import mainWindow
from socket import *
import threading
import detail
import time
import database
import datetime

HOST = '10.8.161.247'
#10.206.12.147
PORT = 8888
BUFSIZ = 1024
ADDR = (HOST, PORT)
MAXCONNECT = 8

work = []
wait = []
clients = []
roomType={'311A':0,'311B':0,'312A':0,'312B':0,'313A':0,'313B':0,'314A':0,'315A':0}

energy={"311A":0.00,"311B":0.00,"312A":0.00,"312B":0.00,"313A":0.00,"313B":0.00,"314A":0.00,"315A":0.00}
cost={"311A":0.00,"311B":0.00,"312A":0.00,"312B":0.00,"313A":0.00,"313B":0.00,"314A":0.00,"315A":0.00}
Money={1:1.00,2:2.00,3:3.00}
Power={1:2.00,2:4.00,3:6.00}
Tempreture={1:0.5,2:0.75,3:1}

class Server(object):

    defaultTemp=26.0
    lowestTemp=18.0
    highestTemp=30.0
    defaultSpeed=1
    mode=0
    lowRate=1
    midRate=2
    highRate=3

    def __init__(self,ui,setting):
        self.ui = ui
        self.tcpSerSock = socket(AF_INET, SOCK_STREAM)
        self.tcpSerSock.bind(ADDR)
        self.tcpSerSock.listen(MAXCONNECT)

        self.defaultTemp = 26.0
        self.lowestTemp = 18.0
        self.highestTemp = 30.0
        self.defaultSpeed = 1
        self.mode = 0
        self.rate = 1

        self.setPara(setting)

        for i in range(8):
            client = Client(self.ui,i, self.mode, self.defaultTemp, self.defaultSpeed, self.lowestTemp, self.highestTemp,self.no_of_service)
            clients.append(client)

    def setPara(self,setting):
        self.defaultTemp=setting['defaultTemp']
        self.defaultSpeed=setting['defaultFan']
        self.lowestTemp=setting['lowest']
        self.highestTemp=setting['highest']
        self.no_of_service=setting['no_of_service']
        if setting['mode']=='制冷':
            self.mode=0
        else:
            self.mode=1




    def run(self):
        threading.Thread(target=self.Switch).start()
        while True:
            print('waiting for connection...')
            Sock, addr = self.tcpSerSock.accept()
            print('Accept new connection from %s:%s...' % addr)
            for i in range(8):
                if clients[i].terminate == 1:
                    clients[i].tcpCliSock = Sock
                    clients[i].addr = addr
                    clients[i].num = i
                    clients[i].terminate = 0
                    threading.Thread(target=clients[i].run).start()
                    break
            #tcpCliSock.close()

    def Switch(self):
        while True:
            time.sleep(10)
            print("wait:", wait)
            print("work", work)
            if len(wait) > 0:
                j = len(wait)
                p = 0
                for i in range(self.no_of_service):
                    if clients[work[i]].vip == 0:
                        if j > p:
                            work.append(wait[p])
                            clients[wait[p]].work = 1
                            wait.remove(wait[p])
                            wait.append(work[i])
                            clients[work[i]].work = 0
                            work.remove(work[i])
                            p = p + 1

				
class Client(object):
    instructions=[]
    def __init__(self,ui,roomnumber,mode,dt,ds,lt,ht,no):#,,0,34.0,1,0.0,50.0
        self.open = 0
        self.tcpCliSock = None
        self.addr = None
        self.ui = ui
        self.mode = mode
        self.num = 0
        self.roomnumber = ''
        self.default_temp = dt
        self.target_temp = dt
        self.speed = ds
        self.Low_temp = lt
        self.High_temp = ht
        self.Cost = 0.00
        self.vip = 0
        self.Energy = 0.00
        self.money = 2.00
        self.temp = 0.0
        self.work = 0
        self.terminate = 1
        self.PAIRING=no

    def set_vip(self):
        self.vip = 1

    def no_vip(self):
        self.vip = 0

    def initialization(self,mode,default_temp,low,high,money):
        self.mode = mode

        self.default_temp = default_temp
        self.Low_temp = low
        self.High_temp = high

        self.money = money

    def mes_detect(self,str):
        if str[0] != '*':
            return -1, []
        slice = str[1:].split('|')
        return int(slice[0]), slice

    def mes_pack(self,list):
        s = '*' + str(list[0])
        for word in list[1:]:
            s = s + '|' + str(word)
        return s


    def message_func(self):
        while self.terminate == 0:
            if self.instructions:
                inslist=self.instructions[0]
                code=int(inslist[0])
                if code == 1:
                    if self.open == 0:
                        self.open = 1
                        self.roomnumber = str(inslist[1])
                        self.temp = float(inslist[2])

                        if roomType[self.roomnumber]==0:
                            self.no_vip()
                        else:
                            self.set_vip()

                        message = ['2', '1', self.mode, float("%.1f" % self.default_temp), self.speed,
                                   float("%.1f" % self.Low_temp), float("%.1f" % self.High_temp), cost[self.roomnumber],
                                   energy[self.roomnumber]]
                        self.send_msg(message)
                        '''
                        self.Signal_target_temp.emit(self.roomnumber, self.target_temp)
                        self.Signal_temp.emit(self.roomnumber, self.temp)
                        self.Signal_target_speed.emit(self.roomnumber, self.speed)
                        self.Signal_speed.emit(self.roomnumber, self.speed)
                        self.Signal_state.emit(self.roomnumber, self.open)
                      '''
                        self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" %self.temp))
                        self.ui.updateTargetTemp(self.roomnumber, ("%.1f" %self.target_temp))
                        self.ui.updateTargetFan(self.roomnumber, self.speed)
                        self.ui.updateCurrentFan(self.roomnumber, self.speed)
                        self.ui.updateState(self.roomnumber, self.open)

                        if len(work) < self.PAIRING:
                            self.work = 1
                            work.append(self.num)
                        else:
                            if self.vip == 1:
                                self.work = 0
                                wait.insert(0, self.num)
                            else:
                                self.work = 0
                                wait.append(self.num)
                            # return pack 2
                            '''
                                                    数据库
                                                    '''
                        database.insertOpenRequest(self.roomnumber, self.open)
                        database.updateStatistics_work_times(self.roomnumber,datetime.datetime.now().strftime('%Y-%m-%d'))
                        database.updateStatistics_report_num(self.roomnumber,
                                                             datetime.datetime.now().strftime('%Y-%m-%d'))
                        database.insertReport(self.roomnumber, code, self.temp, self.target_temp, self.speed,
                                              energy[self.roomnumber], cost[self.roomnumber])


                    else:
                        message = ['2', '0', self.mode, float("%.1f" % self.default_temp), self.speed,
                                   float("%.1f" % self.Low_temp), float("%.1f" % self.High_temp), cost[self.roomnumber],
                                   energy[self.roomnumber]]
                        self.send_msg(message)
                elif code == 3:
                        if inslist[1] == self.roomnumber:
                            self.open = 0
                            self.ui.updateState(self.roomnumber, self.open)
                            self.work = 0
                            message = ['4', '1']
                            self.send_msg(message)
                            self.tcpCliSock.close()
                            self.terminate = 1

                            database.updateStatistics_report_num(self.roomnumber,
                                                                 datetime.datetime.now().strftime('%Y-%m-%d'))
                            database.insertReport(self.roomnumber, code, self.temp, self.target_temp, self.speed,
                                                  energy[self.roomnumber], cost[self.roomnumber])
                        else:
                            message = ['4', '0']
                            self.send_msg(message)
                elif code == 5:
                    if inslist[1] == self.roomnumber:
                        self.speed = int(inslist[2])
                        # self.Signal_speed.emit(self.roomnumber, self.speed)
                        self.ui.updateTargetFan(self.roomnumber, self.speed)
                        self.ui.updateCurrentFan(self.roomnumber, self.speed)
                        # return pack 6
                        '''
                        数据库
                        '''
                        database.insertSpeedRequest(self.roomnumber, self.speed)
                        database.updateStatistics_report_num(self.roomnumber,
                                                             datetime.datetime.now().strftime('%Y-%m-%d'))
                        database.insertReport(self.roomnumber, code, self.temp, self.target_temp, self.speed,
                                              energy[self.roomnumber], cost[self.roomnumber])

                        message = ['6', '1']
                        self.send_msg(message)
                    else:
                        message = ['6', '0']
                        self.send_msg(message)
                elif code == 7:
                    if inslist[1] == self.roomnumber:
                        self.target_temp = float(inslist[2])
                        # self.Signal_target_temp.emit(self.roomnumber, self.target_temp)
                        self.ui.updateTargetTemp(self.roomnumber, ("%.1f" % self.target_temp))
                        # return pack 8
                        '''
                        数据库
                        '''
                        database.insertTempRequest(self.roomnumber, self.target_temp)
                        database.updateStatistics_report_num(self.roomnumber,
                                                             datetime.datetime.now().strftime('%Y-%m-%d'))
                        database.insertReport(self.roomnumber, code, self.temp, self.target_temp, self.speed,
                                              energy[self.roomnumber], cost[self.roomnumber])

                        message = ['8', '1']
                        self.send_msg(message)
                    else:
                        message = ['8', '0']
                        self.send_msg(message)
                elif code == 11:
                    self.temp = float(inslist[2])
                    # self.Signal_temp.emit(self.roomnumber, self.temp)
                    self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
                    if len(work) < self.PAIRING:
                        self.work = 1
                        work.append(self.num)
                    else:
                        if self.vip == 1:
                            self.work = 0
                            wait.insert(0, self.num)
                        else:
                            self.work = 0
                            wait.append(self.num)
                    # into the list
                else:
                    print("code error!")
                    sys.exit()
                self.type_state()
                if self.instructions:
                    self.instructions.remove(self.instructions[0])

    def type_state(self):
        print("state:open:%d" % self.open)
        #print("mode:%d" % self.mode)
        #print("default_temp:%d" % self.default_temp)
        print("target_temp:%f" % self.target_temp)
        print("speed:%d" % self.speed)
        #print("Low_temp:%d" % self.Low_temp)
        #print("High_temp:%d" % self.High_temp)
        #print("Cost:%d" % self.Cost)
        #print("roomNumber:%s" % self.roomnumber)
        #print("Energy:%d" % self.Energy)
        print("temp:%f" % self.temp)
        print("work:%d" % self.work)


    def recv_msg(self):
        while self.terminate == 0:
            try:
                data = self.tcpCliSock.recv(BUFSIZ)
                if not data:
                    break
                code, list = self.mes_detect(str(data, 'utf-8'))
                '''
                数据库
                '''
                #database.insertReport(self.roomnumber, code, self.temp, self.target_temp, self.speed, self.Energy,self.Cost)
                print('\t\t\t',str(data))
                self.instructions.append(list)
            except Exception:
                #terminate代表在线
                print("receive error!")
                self.tcpCliSock.close()
                self.terminate = 1
                self.open = 0
                if self.work == 1:
                    work.remove(self.num)
                    if len(wait)>0:
                        work.append(wait[0])
                        clients[wait[0]].work = 1
                        wait.remove(wait[0])
                self.work = 0
                #self.Signal_state.emit(self.roomnumber, self.open)
                self.ui.updateState(self.roomnumber, self.open)
                break


    def send_msg(self, list):
            data = self.mes_pack(list)
            if not data:
                self.tcpCliSock.close()
            print('\t\t\t',str(data))
            try:
                self.tcpCliSock.send(b'%s' % bytes(data, 'utf-8'))
            except Exception:
                print("send error!")
                sys.exit()

    def temp_control(self):
        if self.target_temp > self.temp and self.target_temp > self.temp + Tempreture[self.speed]:
            if self.mode == 1:
                self.temp = self.temp + Tempreture[self.speed]
                energy[self.roomnumber] = float("%.2f" % (energy[self.roomnumber] + Power[self.speed]))
                cost[self.roomnumber] = float("%.2f" % (energy[self.roomnumber]*Money[self.speed]))
                self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
                self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
                self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
            else:
                self.work = 0
                work.remove(self.num)
                if len(wait) > 0:
                    work.append(wait[0])
                    clients[wait[0]].work = 1
                    wait.remove(wait[0])
                #message = ['10', self.roomnumber]
                #self.send_msg(message)
                self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
                self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
                self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
        elif self.target_temp > self.temp and self.target_temp <= self.temp + Tempreture[self.speed]:
            if self.mode == 1:
                self.temp = self.target_temp
                energy[self.roomnumber] = float("%.2f" % (energy[self.roomnumber] + Power[self.speed]))
                cost[self.roomnumber] = float("%.2f" % (energy[self.roomnumber]*Money[self.speed]))
            self.work = 0
            work.remove(self.num)
            if len(wait) > 0:
                work.append(wait[0])
                clients[wait[0]].work = 1
                wait.remove(wait[0])
            #message = ['10', self.roomnumber]
            #self.send_msg(message)
            self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
            self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
            self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
        elif self.target_temp < self.temp and self.target_temp < self.temp - Tempreture[self.speed]:
            if self.mode == 0:
                self.temp = self.temp - Tempreture[self.speed]
                energy[self.roomnumber] = float("%.2f" % (energy[self.roomnumber] + Power[self.speed]))
                cost[self.roomnumber] = float("%.2f" % (energy[self.roomnumber]*Money[self.speed]))
                self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
                self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
                self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
                # self.Signal_temp.emit(self.roomnumber, self.temp)
                # self.Signal_energy.emit(self.roomnumber, self.Energy)
            else:
                self.work = 0
                work.remove(self.num)
                if len(wait) > 0:
                    work.append(wait[0])
                    clients[wait[0]].work = 1
                    wait.remove(wait[0])
                #message = ['10', self.roomnumber]
                #self.send_msg(message)
                self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
                self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
                self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
        elif self.target_temp < self.temp and self.target_temp >= self.temp - Tempreture[self.speed]:
            if self.mode == 0:
                self.temp = self.target_temp
                energy[self.roomnumber] = float("%.2f" % (energy[self.roomnumber] + Power[self.speed]))
                cost[self.roomnumber] = float("%.2f" % (energy[self.roomnumber]*Money[self.speed]))
            self.work = 0
            work.remove(self.num)
            if len(wait) > 0:
                work.append(wait[0])
                clients[wait[0]].work = 1
                wait.remove(wait[0])
            #message = ['10', self.roomnumber]
            #self.send_msg(message)
            self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
            self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
            self.ui.updateCost(self.roomnumber, ("%.2f" % cost[self.roomnumber]))
        elif self.target_temp == self.temp:
            self.work = 0
            work.remove(self.num)
            if len(wait) > 0:
                work.append(wait[0])
                clients[wait[0]].work = 1
                wait.remove(wait[0])
            #message = ['10', self.roomnumber]
            #self.send_msg(message)
            self.ui.updateCurrentTemp(self.roomnumber, ("%.1f" % self.temp))
            self.ui.updateEn(self.roomnumber, ("%.2f" % energy[self.roomnumber]))
            self.ui.updateCost(self.roomnumber,("%.2f" % cost[self.roomnumber]))
        else:
            print("temp error!")
            sys.exit()


    def run(self):
        #print(len(clients))
        tr = threading.Thread(target=self.recv_msg)
        mf = threading.Thread(target=self.message_func)
        #self.type_state()
        tr.start()
        mf.start()
        while self.terminate == 0:
                if self.work == 1:
                    self.temp_control()
                    message = ['9', self.roomnumber, self.temp, ("%.2f" %energy[self.roomnumber]), ("%.2f" %cost[self.roomnumber])]
                    self.send_msg(message)
                    if self.work == 0:
                        database.updateStatistics_temp_times(self.roomnumber,
                                                             datetime.datetime.now().strftime('%Y-%m-%d'))
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    '''
                    if self.target_temp < self.temp and self.target_temp >= self.temp - self.speed:
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    elif self.target_temp < self.temp and self.target_temp < self.temp - self.speed and self.mode==1:
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    elif self.target_temp > self.temp and self.target_temp > self.temp + self.speed and self.mode==0:
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    elif self.target_temp > self.temp and self.target_temp <= self.temp + self.speed:
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    elif self.target_temp == self.temp:
                        message = ['10', self.roomnumber]
                        self.send_msg(message)
                    '''
                    #self.temp_control()
                time.sleep(5)

class mMainWindow(mainWindow.Ui_MainWindow):
    setting={'mode':'制冷','lowest':18.0,'highest':30.0,'defaultTemp':26.4,'defaultFan':1,'lowRate':1,
             'midRate':2,'highRate':3,'lowP':0.5,'midP':0.75,'highP':1.0,
             'no_of_service':4,
             'roomType':[]}
    started=False
    roomList = ['311A', '311B', '312A', '312B', '313A', '313B', '314A', '315A']

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget.widget(0).setDisabled(True)
        self.tabWidget.widget(1).setDisabled(True)
        self.tabWidget.tabBar().setDisabled(True)
        self.setPushButton.clicked.connect(self.saveSetting)
        self.coldRadioButton.setChecked(True)
        self.defaultFanComboBox.addItem('1',1)
        self.defaultFanComboBox.addItem('2',2)
        self.defaultFanComboBox.addItem('3',3)
        self.serviceNoComboBox.addItem('1', 1)
        self.serviceNoComboBox.addItem('2', 2)
        self.serviceNoComboBox.addItem('3', 3)
        self.serviceNoComboBox.addItem('4', 4)
        self.serviceNoComboBox.addItem('5', 5)
        self.serviceNoComboBox.addItem('6', 6)
        self.serviceNoComboBox.addItem('7', 7)
        self.serviceNoComboBox.addItem('8', 8)
        self.serviceNoComboBox.setCurrentIndex(3)
        self.lowTempLineEdit.setText('18')
        self.highTempLineEdit.setText('30')
        self.defaultTempLineEdit.setText('22')
        self.lowRateLineEdit.setText('1')
        self.midRateLineEdit.setText('2')
        self.highRateLineEdit.setText('3')
        self.lowPLlineEdit.setText('2')
        self.midPineEdit.setText('4')
        self.highPLineEdit.setText('6')
        self.checkBox_1.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_4.setChecked(True)
        self.checkBox_5.setChecked(True)
        self.checkBox_6.setChecked(True)
        self.checkBox_7.setChecked(True)
        self.checkBox_8.setChecked(True)





    def homeTabInit(self):
        if not self.started:
            for i in range(0,len(self.roomList)):
                self.detailtableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.roomList[i]))
                self.detailtableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(roomType[self.roomList[i]])))
                self.detailtableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem('关'))
                self.detailtableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem('--'))
                self.detailtableWidget.setItem(i, 4, QtWidgets.QTableWidgetItem('--'))
                self.detailtableWidget.setItem(i, 5, QtWidgets.QTableWidgetItem('--'))
                self.detailtableWidget.setItem(i, 6, QtWidgets.QTableWidgetItem('--'))
                self.detailtableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem('0'))
                self.detailtableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem('0'))
            self.started=True
        else:
            for i in range(0,8):
                self.detailtableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.setting['roomType'][i]))

        self.modeValuelabel.setText(self.setting['mode'])
        self.rangeValueLabel.setText(str(self.setting['lowest'])+'-'+str(self.setting['highest']))
        #self.rateValueLabel.setText(str(self.setting['rate']))
        self.serviceNoValueLabel.setText(str(self.setting['no_of_service']))
        self.defaultTempValueLabel.setText(str(self.setting['defaultTemp']))


    def saveSetting(self):
        if not self.defaultTempLineEdit.text().isdigit():
            msg=QtWidgets.QMessageBox()
            msg.setText("请输入正确的默认温度！")
            msg.setWindowTitle('错误')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            if self.coldRadioButton.isChecked():
                self.setting['mode']='制冷'
            elif self.hotRadioButton.isChecked():
                self.setting['mode']='制热'
            self.setting['lowest']=float(self.lowTempLineEdit.text())
            self.setting['highest']=float(self.highTempLineEdit.text())
            self.setting['defaultTemp']=float(self.defaultTempLineEdit.text())
            self.setting['defaultFan']=self.defaultFanComboBox.currentData()
            self.setting['lowRate']=float(self.lowRateLineEdit.text())
            self.setting['midRate'] = float(self.midRateLineEdit.text())
            self.setting['highRate'] = float(self.highRateLineEdit.text())
            self.setting['lowP'] = float(self.lowPLlineEdit.text())
            self.setting['midP'] = float(self.midPineEdit.text())
            self.setting['highP'] = float(self.highPLineEdit.text())
            self.setting['no_of_service']=self.serviceNoComboBox.currentData()

            global Money,Power,roomType
            Money[1]=float(self.lowRateLineEdit.text())
            Money[2]=float(self.midRateLineEdit.text())
            Money[3]=float(self.highRateLineEdit.text())
            Power[1]=float(self.lowPLlineEdit.text())
            Power[2]=float(self.midPineEdit.text())
            Power[3]=float(self.highPLineEdit.text())

            if self.checkBox_1.isChecked():
                roomType['311A'] = 0
            else:
                roomType['311A'] = 1

            if self.checkBox_2.isChecked():
                roomType['311B'] = 0
            else:
                roomType['311B'] = 1

            if self.checkBox_3.isChecked():
                roomType['312A'] = 0
            else:
                roomType['312A'] = 1

            if self.checkBox_4.isChecked():
                roomType['312B'] = 0
            else:
                roomType['312B'] = 1

            if self.checkBox_5.isChecked():
                roomType['313A'] = 0
            else:
                roomType['313A'] = 1

            if self.checkBox_6.isChecked():
                roomType['313B'] = 0
            else:
                roomType['313B'] = 1

            if self.checkBox_7.isChecked():
                roomType['314A'] = 0
            else:
                roomType['314A'] = 1

            if self.checkBox_8.isChecked():
                roomType['315A'] = 0
            else:
                roomType['315A'] = 1

            self.homeTabInit()
            self.tabWidget.widget(0).setEnabled(True)
            self.tabWidget.widget(1).setEnabled(True)
            self.tabWidget.tabBar().setEnabled(True)
            self.tabWidget.setCurrentIndex(0)

            self.thread=WorkThread(self)
            self.thread.setPara(self.setting)
            self.thread.start()

    # 更新目标温度
    def updateTargetTemp(self,id,temp):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(str(temp)))


    # 更新当前温度
    def updateCurrentTemp(self,id,temp):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i,4,QtWidgets.QTableWidgetItem(str(temp)))

    # 更新目标风速
    def updateTargetFan(self,id,fan):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(fan)))

    # 更新当前风速
    def updateCurrentFan(self,id,fan):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i,6,QtWidgets.QTableWidgetItem(str(fan)))

    # 更新当前开关机状态
    def updateState(self,id,state):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        if state == 1:
            self.detailtableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem('开'))
        elif state == 0:
            self.detailtableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem('关'))
        else:
            self.detailtableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem('error'))
    # 更新当前能耗和费用
    def updateEnAndCost(self,id,energy):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(energy)))
        self.detailtableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(energy*self.setting['rate'])))

    def updateEn(self,id,energy):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i, 7, QtWidgets.QTableWidgetItem(str(energy)))

    def updateCost(self,id,cost):
        for i in range(0,len(self.roomList)):
            if self.roomList[i]==id:
                break
        self.detailtableWidget.setItem(i, 8, QtWidgets.QTableWidgetItem(str(cost)))


class WorkThread(QThread):
    #trigger = pyqtSignal(mMainWindow)

    def __init__(self,UI,parent = None):
        super(WorkThread, self).__init__()
        self.ui = UI
    def run(self):
        #self.trigger.emit()
        self.server = Server(self.ui,self.setting)
        self.server.run()

    def setPara(self,setting):
        self.setting=setting

if __name__ == '__main__':
    app=QApplication(sys.argv)
    mWindow=QMainWindow()
    ui=mMainWindow()
    ui.setupUi(mWindow)
    #thread = WorkThread(ui)
    #thread.start()
    #server=Server(ui)
    #threading.Thread(target=server.run)
    mWindow.show()
    sys.exit(app.exec_())
