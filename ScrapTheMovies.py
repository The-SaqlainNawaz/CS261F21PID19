from os import write
from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QApplication, QTableView
#from PyQt5.QtCore import QAbstractTableModel, Qt
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from NewScrap import Ui_MainWindow
import pandas as pd
import threading
import csv
from datetime import datetime
import Sorting as algo

pause = False
p_count = 0
stop = False

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       # u = uic.loadUi('ScrapTheFuckingMovies.ui', self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.closebutton.clicked.connect(lambda: self.close())
        self.ui.pushButton_4.clicked.connect(lambda: self.showMinimized())
        self.Main_list=[]

        #################################################################################
        ############################### List of Objects of classes in Sorting ###########
        #################################################################################
        self.Sortingg =[algo.Selection_Sort(),algo.Insertion_Sort(),algo.Quick_Sort(),algo.Merge_Sort(),algo.Bubble_Sort(),algo.Hybrid_Sort(),algo.CockTail_Sort()]


        #################################### initally scrp movie list is disabbled #############
        self.ui.scrap_btn.setEnabled(False)
        ########################################################################################
        self.show()
        self.ui.pushButton.setEnabled(False)
        

        # Call to import file
        self.ui.pushButton_2.clicked.connect(self.exportfile)
        self.ui.pushButton_2.clicked.connect(self.Form2DImp)

        #Call for start Scrapping
        ##############################################################
        #################### Connecting the functions################
        #############################################################
        self.ui.startbutton.clicked.connect(self.start_Scrap)
        self.ui.startbutton_2.clicked.connect(self.Pause_Scrap)
        self.ui.startbutton_3.clicked.connect(self.Stop_Scarp)
        self.ui.startbutton_3.clicked.connect(self.Enable)
        self.ui.pushButton.clicked.connect(self.Save_file)
        # Connect for maiking 2d array from scrap method
        self.ui.scrap_btn.clicked.connect(self.Form2DArr)
        # Connect Sort button with Sort
        self.ui.pushButton_3.clicked.connect(self.Sort)
        
        


       # self.close()
    def Enable(self):
        self.ui.pushButton.setEnabled(True)   

    # Threading is done to do mutilpe task   
    def exportfile(self):
        thread = threading.Thread(target= self.export)
        thread.start()

    # Function to impoort csv file from pc into tables
    def export(self):
        file_name = self.ui.lineEdit_2.text()
        file_name = file_name + ".csv"
        try:
            with open(file_name, "r",encoding="utf-8") as fileInput:
                roww = 0
                data = list(csv.reader(fileInput))
                for row in data:
                    self.ui.tableWidget.setRowCount(len(data))
                    self.ui.tableWidget.setItem(roww, 0 , QtWidgets.QTableWidgetItem((row[0])))
                    self.ui.tableWidget.setItem(roww, 1 , QtWidgets.QTableWidgetItem((row[1])))
                    self.ui.tableWidget.setItem(roww, 2 , QtWidgets.QTableWidgetItem((row[2])))
                    self.ui.tableWidget.setItem(roww, 3 , QtWidgets.QTableWidgetItem((row[3])))
                    self.ui.tableWidget.setItem(roww, 4 , QtWidgets.QTableWidgetItem((row[4])))
                    self.ui.tableWidget.setItem(roww, 5 , QtWidgets.QTableWidgetItem((row[5])))
                    self.ui.tableWidget.setItem(roww, 6 , QtWidgets.QTableWidgetItem((row[6])))
                    self.ui.tableWidget.setItem(roww, 7 , QtWidgets.QTableWidgetItem((row[7]))) 
                    #self.ui.tableWidget.setItem(roww, 8 , QtWidgets.QTableWidgetItem((row[8])))  
                    roww += 1       
        except:
            print("Sorry File not Find --)")  
    def Scrapping(self):
        now = datetime.now()
        #string_time = now.strftime("%H:%M:%S")
        headers = {"Accept-Language": "en-US,en;q=0.5"}
        movie_title = []
        year = []
        rating=[]
        director =[]
        cast = []
        synop = []
        genre=[]
        movie_duration=[]
        global pause,stop
        number = int(self.ui.lineEdit_6.text())
        pages = np.arange(number)
        basic_link="/search/title/?release_date=1980-01-01,2019-10-31"
        for page in pages:
            if(stop==True):
                break
            while (pause):
                None
            add_end="&ref_=adv_nxt"
            cast1 =[]
            add_st="https://www.imdb.com"
            full_link=add_st+basic_link+add_end
            page = requests.get(full_link)
            soup = BeautifulSoup(page.text, 'html.parser')
            movie_data = soup.findAll('div', attrs = {'class': 'lister-item mode-advanced'})
            sleep(randint(2,5))
            for info in movie_data:
                name= info.find('div',class_="lister-item-content").find('h3',class_="lister-item-header").find('a').text
                #name = info.h3.a.text
                movie_title.append(name)
                
                # year of release
                release = info.find('h3',class_="lister-item-header").find('span',class_="lister-item-year text-muted unbold").text
                ab=release.split("–")
                
                if(len(ab)==2):
                    if(ab[1]!=" )"):    
                        bn=ab[0]+str("-")+ab[1]
                        year.append(bn)
                    else:
                        year.append(ab[0])
                elif(len(ab)==1):
                    year.append(ab[0])   

                try:
                    rate= info.find('div',class_="ratings-bar").find('div',class_="inline-block ratings-imdb-rating").find('strong').text
                    rating.append(rate)
                except:
                    rating.append(0)
                
                # Description of the Movies
                try:
                    describe = info.findAll('p', class_ = 'text-muted')
                    description_ = describe[1].text.replace('\n', '') if len(describe) >1 else '*'
                    if(description_=="Add a Plot"):
                        synop.append("N/A")
                    else:
                        synop.append(description_)
                except:
                    print("no description")
                    synop.append("N/A")
                try:
                    
                    direct=info.find('div',class_="lister-item-content").find_all('p')
                    dr=direct[2].find_all('a') if direct[2].find_all('a') else director.append("N/A")
                    dr=direct[2].find_all('a') if direct[2].find_all('a') else cast.append("N/A") and cast1.append("N/A")
                    #print(dr)
                    dire=dr[0].text
                    director.append(dire)
                    cst=[]
                    if(len(dr)>1):
                        for i in range(1,len(dr)):
                            cst.append(dr[i].text)
                        cast.append(cst)
                        cast1.append(cst)           
                    else:
                        cast.append("N/A")
                        cast1.append("N/A")
                    gen=info.find('div',class_="lister-item-content").find('span',class_="genre").text.replace('\n','').replace('            ','')    
                    #gen=info.find('div',class_="lister-item-content").find('span',class_="genre").text.replace('\n','')
                    # duration of the movie
                    tim = info.p.find('span', class_ = "runtime").text if info.p.find('span', class_ = "runtime").text else "N/A"
                    genre.append(gen)
                # print(tim)
                    movie_duration.append(tim)

                except:
                # director.append("N/A ")
                # cast.append("N/A")
                    genre.append("N/A")
                    movie_duration.append("N/A")
                   
                       
                    
            next_pagelink=soup.find('div', attrs = {'class': 'desc'})
            nextt=next_pagelink.find('a',class_="lister-page-next next-page")
            kk=nextt['href']
            #print(kk)
            basic_link=""
            basic_link=kk
            r=0
            j=0
            #sleep(5)
            for row in range(len(movie_title)):
                self.ui.tableWidget.setRowCount(len(movie_title))
                self.ui.tableWidget.setItem(r,0,QtWidgets.QTableWidgetItem(movie_title[j]))
                self.ui.tableWidget.setItem(r,1,QtWidgets.QTableWidgetItem(movie_duration[j]))
                self.ui.tableWidget.setItem(r,2,QtWidgets.QTableWidgetItem(year[j]))
                self.ui.tableWidget.setItem(r,3,QtWidgets.QTableWidgetItem(genre[j]))
                self.ui.tableWidget.setItem(r,4,QtWidgets.QTableWidgetItem(rating[j]))
                self.ui.tableWidget.setItem(r,5,QtWidgets.QTableWidgetItem(director[j]))
                self.ui.tableWidget.setItem(r,7,QtWidgets.QTableWidgetItem(synop[j]))
                st=""
                jy=""
                final_cast=''
                k=0
                for i in cast:
                    st =(i)
                    #print(st)
                    for jl in st:
                        jy=jl
                        #print(jy)
                        final_cast =final_cast+ jy+" , "
                    #print(final_cast)    
                    self.ui.tableWidget.setItem(k,6,QtWidgets.QTableWidgetItem(final_cast))
                    final_cast=""
                    k+=1   
                r +=1
                j +=1             

        end = datetime.now()
        #end_time = end.strftime("%H:%M:%S")
        time = (end - now)
        #print(time)
        self.ui.lineEdit_3.setText(str(time))
        self.ui.lineEdit_4.setText(str(number*50))
        self.ui.pushButton.setEnabled(True)
      #  movie_list = pd.DataFrame({ "Movie Name": movie_title,"Duration":movie_duration,"Year of Release" : year, "Gnere": genre,"Movie Rating": rating, "Direcror": director, "Cast" : cast, "Description": synop})
      #  movie_list.to_csv("scrapData01.csv")
    
    # threading of Scraping
    def start_Scrap(self):
        thread = threading.Thread(target= self.Scrapping)
        thread.start()

    def Pause_Scrap(self):
        global pause,p_count
        if(p_count==0):
            pause = True
            self.ui.startbutton_2.setText("Resume")
            p_count = 1
        else:
            pause = False
            p_count = 0
            self.ui.startbutton_2.setText("Pause")

    def Stop_Scarp(self):
        global stop
        stop = True

    def Save_file(self):
        total_row = self.ui.tableWidget.rowCount()                
        for i in range(total_row):
            movie_list=[]
            movie_list.append(self.ui.tableWidget.item(i,0).text())
            movie_list.append(self.ui.tableWidget.item(i,1).text())
            movie_list.append(self.ui.tableWidget.item(i,2).text())
            movie_list.append(self.ui.tableWidget.item(i,3).text())
            movie_list.append(self.ui.tableWidget.item(i,4).text())
            movie_list.append(self.ui.tableWidget.item(i,5).text())
            movie_list.append(self.ui.tableWidget.item(i,6).text())
            movie_list.append(self.ui.tableWidget.item(i,7).text())
            with open("MoviesScrapped.csv",'a+',encoding="utf-8",newline='')as file:
    
                myfile = csv.writer(file)
                myfile.writerow(movie_list)
                self.ui.scrap_btn.setEnabled(True)

    def Form2DArr(self):
        name = "MoviesScrapped.csv"
        self.Main_list=algo.fromScrapList(name)
        self.ui.pushButton_2.setEnabled(False)

    
    def Form2DImp(self):
        file_name = self.ui.lineEdit_2.text()
        file_name = file_name + ".csv"
        self.Main_list=algo.fromImport(file_name)
        self.ui.scrap_btn.setEnabled(False)
    

    def Sort(self):
        if(self.ui.Ascend.isChecked()):
            al = self.ui.comboBox.currentIndex()
            col = self.ui.comboBox_2.currentIndex()
            if(al == 0 or al==1 or al == 4):
                self.Main_list=self.Sortingg[al].Asc(self.Main_list,col)
                self.PrintInTable()
            elif( al==2 or al==3 or al==5 or al==6):
                size=len(self.Main_list)
                if(al==3):
                    self.Sortingg[al].Asc(self.Main_list,0,size,col)
                    self.PrintInTable()
                else:
                    self.Sortingg[al].Asc(self.Main_list,0,size-1,col)
                    self.PrintInTable()    
            #elif(al==2):
            #    algo.Quick_Asc(self.Main_list,0,len(self.Main_list)-1,col)
            #    self.PrintInTable()    
            else:
                self.Main_list=algo.Tree_Sort_Asc(self.Main_list,col)
                self.PrintInTable()                


    ################### To Print Data in table through list after sorting#############
    ##################################################################################3
    def InTable(self):
        thread=threading.Thread(target=self.PrintInTable)
        thread.start()
    def PrintInTable(self):
        row =0
        self.ui.tableWidget.setRowCount(len(self.Main_list))
        for i in self.Main_list:
            self.ui.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i[0]))
            self.ui.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(i[1])+" min"))
            self.ui.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(i[2]))
            self.ui.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
            self.ui.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
            self.ui.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(i[5]))
            self.ui.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(i[6]))
            self.ui.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(i[7]))
            row+=1

    

#self.ui.pushButton.clicked.connect(exportfile())
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()