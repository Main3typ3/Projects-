from tkinter import*
from tkinter import ttk
import tkinter as tk
import math
import os
import tkinter.messagebox
import sqlite3
import random
from tkinter.messagebox import showinfo

#-------------------------CREATE_DATABASE------------------#
conn = sqlite3.connect('SCOPE.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Login (LoginID INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT, password TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS UserInfo(userID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, email TEXT,postcode TEXT,phoneN0 TEXT,UserAdmin TEXT)''')
#cursor.execute('''CREATE TABLE IF NOT EXISTS JobSceen(jobID INTEGER PRIMARY KEY AUTOINCREMENT,starrating FLOAT,reviews TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS OfferJob (OfferID INTEGER PRIMARY KEY AUTOINCREMENT,jobID TEXT,LoginID_OWNER_JOB TEXT, LoginID_OFFER_JOB TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS AddJob( jobID INTEGER PRIMARY KEY AUTOINCREMENT, jobtitle TEXT,jobdescription TEXT,Name TEXT,JobPrevious TEXT,JobPay TEXT,JOBHOURS TEXT,LoginID)''')


#-----------------------------------------------------------LOGIN PAGE-----------------------------------------------------------------------------------#
class window():
    def __init__(self,master):
        self.master = master                                    # creates a canvas empty
        self.master.geometry("450x600")                         #sets the sizing of page
        self.master.config(bg="CadetBlue1")                     #creates background colour 
        self.master.title("SCOPE LOGIN PAGE")                   #names canvas
        
#----------------LOGIN TITLE---------#
        
        self.MAINTITLE = Label(self.master,text = "SCOPE LOGIN PAGE",bg="CadetBlue1",font = ("Ariel", 20, "bold"))   #names the Large Title above the page                                                                                       # puts it onto the page
        self.MAINTITLE.place(x=70,y=20)                                                                              #places the coordinates 
        self.logintitle = Label(self.master,text = "Enter your login details below:",bg="CadetBlue1",font=(2))    # creates title to state where to put in details                                                                                  # puts this onto the screen
        self.logintitle.place(x=55,y=200)                                                                         #  puts this onto the screen
#-------------------LOGO---------------------------#
        photo = PhotoImage(file='smallscope2.png')
        self.label = Label(image=photo)
        self.label.image= photo
        self.label.place(x=100, y=100)
        
#----------USERNAME SECTION-------#
        
        self.Username = Label(self.master,text ="Username:",bg="CadetBlue1")   #creates a label called username                                                   
        self.Username.place(x=50,y=240)                                        #packs this username onto those cooridates 

        self.Usernameinput = Entry(self.master,bd =3)     #creates a userinput with a boarder
        self.Usernameinput.place(x=140,y=240)             #places the coordinates 

#-----------PASSWORD SCTION-------#

        self.Password = Label(self.master,text ="Password:",bg="CadetBlue1")    #creates password label that gets                             
        self.Password.place(x=50,y=270)                   # places the coordinates 
        
        self.Passwordinput = Entry(self.master,bd =3,show = "*")     #creates a userinput with a boarder
        self.Passwordinput.place(x=140,y=270)             #places the coordinates 


       
            
 #------------BUTTONS-------------#
        
        self.createbtn = Button(self.master, text ="Create An Account",font=('arial',8,'bold'),height= 2, width=15,command = self.gotoCreateAccount) 
        self.createbtn.place(x=40,y=350)

        self.loginbtn = Button(self.master,text="Log In",font=('arial',8,'bold'), height=2, width= 15,command = self.verifylogin)
        self.loginbtn.place(x=165,y=350)

        self.Quit = Button(self.master,text="Quit Application",font=('arial',8,'bold'), height=2, width=15,command = self.ConfirmExit) 
        self.Quit.place(x=290,y=350)
        
#-----------BUTTON_METHODS for exiting ----------#
        
    def ConfirmExit(self):
            
        ConfirmExit = tkinter.messagebox.askyesno("SCOPE CLIENT","ARE YOU SURE YOU WANT TO CLOSE SCOPE CLIENT ")
        if ConfirmExit > 0:
            self.master.destroy()
            return
    #-----------------------BUTTON_METHODS for going to job window --------------------------------------------#
        
    def Gotojobwindow(self):
        root1 = Toplevel(self.master)
        jobGUI = jobwindow(root1)
        
    #---------------------BUTTON_METHODS for creating a new account ----------------------------------------------#
        
    def gotoCreateAccount(self):
        root2 = Toplevel(self.master)
        AccGUI = Create_Account_page(root2)
        
    #------------------------method for verifying the login details -------------------------------------------#   
    def verifylogin (self):

        #------------------------------------GRABS USERNAME AND PASSWORD FROM LOGIN --------------------------------------------------------------------------------------
        
        username = self.Usernameinput.get()
        password = self.Passwordinput.get()
        
        #--------------------------------------CHECKS DATABASE IF ANY USERNAME IS THE SAME AS FETCHED USERNAME INPUTTED------------------------------------------------------------------------------------

        cursor.execute("Select * FROM Login WHERE username = (?)",(username,))
        conn.commit()
        info = cursor.fetchone()
        
        #----------------------------TRYS TO PUT THE USERNAME AND PASSWORD SAVED INTO VARIABLES----------------------------------------------------------------------------------------------

        try:
            
            UserID_sql = info[0]
            username_sql = info[1]
            password_sql = info[2]
            
        #----------------TRIES TO GLOBALISE THE CURRENT USERNAME AND THE CURRENT USERID----------------------------------------------------------------------------------------------------------
            global UserIDSQL_GLOBAL
            UserIDSQL_GLOBAL = UserID_sql
            
            global USERNAMEsql_GLOBAL
            USERNAMEsql_GLOBAL = username_sql
        #----------------------------IF THE USERNAME IS NOT FOUND IN THE DATABASE EMPTY USER IS ASSIGNED ----------------------------------------------------------------------------------------------
        except:
            username_sql = ""
            password_sql= ""
        #-----------------------------IF THE USER DOESNT INPUT ANYTHING THE CODE TELLS THE USER TO LEAVE SOMETHING IN THE BOX ---------------------------------------------------------------------------------------------

        if username == "" or password == "":
            
        #-----------------------THIS TRY COLLAPSES ANY OLD LABELS BEFORE PLACING NEW ONES ---------------------------------------------------------------------------------------------------    

            try:
               self.wrong_password.destroy()
               self.fail_login.destroy()
            except:
                pass
                
        #--------------------------------------------------------PLACES LABEL IF USER DOESNT ENTER ANYTHING------------------------------------------------------------------

            self.empty_login_label = Label(self.master,text = "DONT LEAVE ENTERY BOXES EMPTY",bg="CadetBlue1",foreground = "red",font = ("Ariel", 10, "bold"))
            self.empty_login_label.place(x=110,y=300)
            
        #--------------------------------------IF THE FETCHED DATA IS EMPTY THEN THE ACCOUNT DOESNT EXIST ------------------------------------------------------------------------------------    

        elif username_sql == "" and password_sql == "":
            
            #-----------------------THIS TRY COLLAPSES ANY OLD LABELS BEFORE PLACING NEW ONES --------------------------------------------------------------------------------------------

            try:
               self.empty_login_label.destroy()
               self.wrong_password.destroy()
            except:
                pass
                
            #----------------------------THE LABEL ACCOUNT DOESNT EXIST IS OUTPUTTED ---------------------------------------------------------------------------------------------- 

            self.fail_login = Label(self.master,text = "ACCOUNT DOES NOT EXIST",bg="CadetBlue1",foreground = "red",font = ("Ariel", 10, "bold"))
            self.fail_login.place(x=110,y=300)
            
            #-------------------------------------IF THE FETCHED DATA MATCHES UP WITH THE INPUTTED DATA THEN CODE GOES TO JOB WINDOW------------------------------------------------------------------------------------- 

        elif username_sql == username and password_sql == password:
            self.Gotojobwindow()
            
            #--------------else try destory any lables that are obstructing the view and display incorrect password on screen -----------------------------------------

        else:
            try:
               self.empty_login_label.destroy()
               self.fail_login.destroy()
            except:
                pass
            self.wrong_password = Label(self.master,text = "INCORRECT PASSWORD PLEASE TRY AGAIN",bg="CadetBlue1",foreground = "red",font = ("Ariel", 10, "bold"))
            self.wrong_password.place(x=100,y=300)
            
            #-------------------------------------------------------------------------------------------------------------------------- 
        

        
#-------------------------------------------------------------CREATE ACCOUNT PAGE----------------------------------------------------------------------#
        
class Create_Account_page(): 
#----------------------------------------constructor-------------#
    def __init__(self, master):

        self.master = master
        self.master.title("Create an account")
        self.master.config(bg="CadetBlue1")
        self.master.geometry("400x400") 
        self.Accdetails = Label(self.master, text ="Enter your new Account Details",bg="CadetBlue1",font= ("Ariel", 10, "bold")) 
        self.Accdetails.place(x=80,y=20)
#-----------USERNAME---------------------#
        self.Acc_username = Label(master, text="Enter a username:",bg="CadetBlue1")
        self.Acc_username.place(x=50,y=50)
         
        self.Acc_username = Entry(master)
        self.Acc_username.place(x=160,y=50)

#-------------------PASSWORD------------------#        
        self.Acc_password = Label(master, text="Enter a password:",bg="CadetBlue1")
        self.Acc_password.place(x=50,y=80)
        
        self.Acc_password = Entry(master,show = "*")
        self.Acc_password.place(x=160,y=80)

#----------------NAME-----------------------#
        self.Name = Label(master,text = "Enter your name:",bg="CadetBlue1")
        self.Name.place(x=50,y=110)

        self.Name = Entry(master)
        self.Name.place(x=160,y=110)
#-------------EMAIL ADDRESS------------------#
        self.email = Label(master,text = "Enter your EMAIL:",bg="CadetBlue1")
        self.email.place(x=50,y=140)

        self.email = Entry(master)
        self.email.place(x=160,y=140)
#---------------------POSTCODE---------------#
        self.postcode = Label(master,text = "Enter Postcode:",bg="CadetBlue1")
        self.postcode.place(x=50 ,y=170 )

        self.postcode= Entry(master)
        self.postcode.place(x=160 ,y=170 )
#---------------PHONE NUMBER----------------#
        self.Phone = Label(master,text = "Enter Phone N0:",bg = "CadetBlue1")
        self.Phone.place(x=50,y=200)
        
        self.Phone = Entry(master)
        self.Phone.place(x=160,y=200)


#--------------------Tick BOX ADMIN ACCOUNT -------------------#
        self.admin_tickbutton = Checkbutton(master, text = "Admin Account",bg="CadetBlue1", command = self.ADMIN_ACCOUNT)
        self.admin_tickbutton.place(x=20,y=290)
        
        


#---------------BUTTON_COMMAND----------------#
        
            
        self.create_account = Button(master, text = 'Create Account', command =  self.create_acc_code)
        self.create_account.place(x=150,y=290)
        
#--------------------QUIT BUTTON----------------------------#
        
        self.quit_button = Button(master, text = 'Quit Application ', command = self.ConfirmExit)
        self.quit_button.place(x=250,y=290)
#------------------------------------------------#
        
    def ADMIN_ACCOUNT(self):
        #------------------------------asking to enter admin key on destruction of the tick box-----------------------------------------#
        self.admin_tickbutton.destroy()
        self.AdminLabel = Label(self.master,text = "Enter Known unique admin code:",bg="CadetBlue1")
        self.AdminLabel.place(x=1,y=230)
        self.AdminAccount_input = Entry(self.master,bd =1, width=17, font=('Arial 10'),show="*")
        self.AdminAccount_input.place(x=200, y =230)

        
        
    #---------------- destory the display button method------#
        
    def ConfirmExit(self):
      self.master.destroy()
      
            
    def create_acc_code(self):
        #--------------------------fetching data from inputs -------------------------------------------------
        user = self.Acc_username.get()
        passw = self.Acc_password.get()
        Name = self.Name.get()
        email = self.email.get()
        postcode = self.postcode.get()
        phone = self.Phone.get()
        #------------------------------checking if user has inputted any admin key--------------------------------------------
        try:
            
            adminaccount = self.AdminAccount_input.get()
        except:
            adminaccount = ""
       #---------------------------------------------------------------------------
           
        #------------------------------CAPTURING USERNAME FROM DATABASE WHICH IS IDENTICAL TO USER ----------------------------------------------------------   
        cursor.execute("Select username FROM Login WHERE username = (?)",(user,))
        conn.commit()
        userinfo= cursor.fetchone()
        #---------------------------CHECKING DATA BASE IF ANY USERNAMES ARE LIKE ONE INPUTTED----------------------------------------------------
        try:
            
           Username_capture_sql = userinfo[0]

        except:
            Username_capture_sql = ""
            
        #--------------------CHECKING IF USER HAS PUT IN CORRECT ADMIN CODE TO BE ADMIN-------------------------------------------------
        if adminaccount == "admin" or adminaccount == "Admin":
            user_is_an_admin = "True"
            
        else:
            user_is_an_admin = "False"
        #---------------------------------------------------CHECKING IF ALL INPUT BOXES HAVE BEEN FILLED IN ----------------------------------------------------------------------------
            
        if user == "" or passw == "" or Name == "" or email == "" or postcode == "" or phone == "":
            try:
                self.Short_username.destroy()
                self.exisiting_account.destroy()
                
            except:
                pass
            self.empty_entry_box = Label(self.master, text = """Dont leave Entry boxes Empty""",font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
            self.empty_entry_box.place(x=70,y=260)
        #-----------------------------CHECKING IF PASSWORD AND USERNAME IS LONGER THAN 5 LETTERS-------------------------------------------------------------------------------   
        elif len(user) < 5 or len(passw) < 5:
          try:
              self.exisiting_account.destroy()
              self.empty_entry_box.destroy()
          except:
              pass
          
          self.Short_username = Label(self.master, text = """Username and Password need to be longer than 6 characters""",font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
          self.Short_username.place(x=1,y=260)
        #------------------------------------------CHECKING IF USERNAME HAS BEEN TAKEN YET-------------------------------------------------------------------------------------------
        elif Username_capture_sql == user:
          try:
              self.Short_username.destroy()
              empty_entry_box.destroy()
              
          except:
              pass
              
          self.exisiting_account = Label(self.master, text = """USERNAME TAKEN ,TRY A DIFFERENT USERNAME""",font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
          self.exisiting_account.place(x=70,y=260)
          #------------------------------------------------INSERTING VALUES INTO DATABASE s------------------------------------------------------------------------------------------------------------------------
        else:
          cursor.execute('INSERT INTO Login VALUES (NULL,?,?)',(user,passw))
          conn.commit()
          cursor.execute('INSERT INTO UserInfo VALUES (NULL,?,?,?,?,?)',(Name,email,postcode,phone,user_is_an_admin))
          conn.commit()
          self.accountmade = Label(self.master,text="Your account has been made",font  = ("Ariel", 10, "bold"),bg="CadetBlue1")
          self.accountmade.place(x=110,y=350)
          self.master.destroy()
          #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class jobwindow():
    
    def __init__(self, master):
        self.master = master
#----------------------------------TITLE----------------------------------------------#
        self.master.title("Scope Job Window") 
        self.master.geometry("1220x700")
        self.master.config(bg="CadetBlue1")
#------------------------------------------SUB TITLE--------------------------------------#
        Loginpage_label = Label(self.master, text ="SCOPE JOB PAGE", font=("Ariel", 20, "bold"),bg="CadetBlue1").pack()
#----------------------------------LOGO IMAGE-----------------------------------------------#
        picture = PhotoImage(file='smallscope3.png')
        self.label = Label(master,image=picture)
        self.label.image= picture
        self.label.place(x=550, y=75)
#----------------------------------------QUIT BUTTON-------------------------------------------#
        self.quit_button = Button(master, text = 'Quit Application', font=('arial',8,'bold'),height= 2, width=15,command =self.ConfirmExit)
        self.quit_button.place(x=795,y=210)
#-----------------------------------------------FILTER BUTTON-------------------------------------#
        self.Filter_button = Button(master, text = 'Filter',font=('arial',8,'bold'),height= 2, width=15, command =self.filter_button )
        self.Filter_button.place(x=200,y=210)
#----------------------------------------------SEARCH FOR BUTTON----------------------------------------#
        self.search_for_button = Button(master, text = 'Search For',font=('arial',8,'bold'),height= 2, width=15, command =self.Search_for_Button )
        self.search_for_button.place(x=110,y=160)
#----------------------------------------------DELETE JOB BUTTON----------------------------------------#
        self.Delete_job_button = Button(master, text = 'Delete job',font=('arial',8,'bold'),height= 2, width=15, command =self.Delete_job )
        self.Delete_job_button.place(x=560,y=210)
#-----------------------------------------LIST MY JOBS BUTTON----------------------------------------------#
        self.list_my_jobs_button = Button(master, text = 'List my jobs',font=('arial',8,'bold'),height= 2, width=15, command =self.list_my_jobs )
        self.list_my_jobs_button.place(x=678,y=210)
#-----------------------------------------APPLY FOR JOB BUTTON----------------------------------------------#
        self.apply_for_jobs_button = Button(master, text = 'Offer a Job',font=('arial',8,'bold'),height= 2, width=15, command =self.apply_for_jobs )
        self.apply_for_jobs_button.place(x=440,y=160)
#-----------------------------------------SEARCH FOR INPUT----------------------------------------------#        
        self.searchinput = Entry(self.master,bd =3, width=17, font=('Arial 15'))     #creates a userinput with a boarder
        self.searchinput.place(x=240,y=163) # puts this onto the screen
#-------------------------------------------ADD JOB BUTTON---------------------------------------------#
        self.Add_job_button = Button(master, text = 'Add Job', font=('arial',8,'bold'),height= 2, width=15,command =self.Add_job)
        self.Add_job_button.place(x=320,y=210)
#-----------------------------------------VIEW OFFERS-----------------------------------------------------------#
        self.View_Offers_button = Button(master, text = 'View my offers', font=('arial',8,'bold'),height= 2, width=15,command =self.View_offers)
        self.View_Offers_button.place(x=1000,y=210)
#-----------------------------------------LOGGED IN AS----------------------------------------------------------#
        self.current_userID = UserIDSQL_GLOBAL
        self.current_username = USERNAMEsql_GLOBAL
        
        self.Acc_password = Label(master,text = "You are logged in with Username: "+str(self.current_username) ,font=("Ariel", 10, "bold"),bg="CadetBlue1")
        self.Acc_password.place(x=10,y=10)
#--------------------------------------------REFRESH BUTTON--------------------------------------------#
        self.Refresh = Button(master, text = 'Refresh Page',font=('arial',8,'bold'),height= 2, width=15, command =self.ADDjob_to_tree_view_refresh)
        self.Refresh.place(x=440,y=210)
#---------------------------------------------Show more info button-------------------------------------#
        self.MoreJobDescription = Button(master, text = "More Job Description Info",font=('arial',8,'bold'),height= 2, width=25, command = self.Show_More_Information)
        self.MoreJobDescription.place(x=560,y=160)
#----------------------------------FILTER OPTIONS ------------------------------------------------------#
     
        # options for dropdown
        Options = [
        'programmer',
        'plumber',
        'banker',
        'accountant',
        'teacher',
        'builder',
        'manager',
        'event worker',
        'waiter',
        'actor',
        'receptionist',
        'personal assistant',
        'personal trainer',
        'dentist'
        
        ]
        self.filterchoice = StringVar(master)
        self.filterchoice.set("Quick Filter")
        #dropdown
        self.Dropdown = OptionMenu(master,self.filterchoice,*Options,)
        self.Dropdown.place(x=90,y=210)
        
#-----------------------------------TREE VIEW CONFIG AND WIDTH LENGTH/ FONT / STYLE -----------------------------------------------------#
        # Create a tree view table
        self.style = ttk.Style()
        self.style.theme_use("alt")
        self.style.configure("Treeview", background ="silver",foreground = "black", rowheight= 35, fieldbackground="silver" )
        self.style.map("Treeview",background=[("selected","light green")])
        self.tree = ttk.Treeview(master,)
        # Add columns to the tree view table
        self.tree["columns"] = ("0", "1", "2","3","4","5")

        # Set the column headers
        self.tree.heading("#0", text="JOB TITLE")
        self.tree.heading("#1", text="JOB DESCRIPTION")
        self.tree.heading("#2", text="NAME")
        self.tree.heading("#3", text="EXPECTED JOB RATES")
        self.tree.heading("#4", text="PREVIOUS JOB TITLE")
        self.tree.heading("#5", text="EXPECTED HOURS TO WORK")
        self.tree.heading("#6", text="JOB ID")
        
        # Pack the tree view table to the root window
        self.tree.place(x=10, y = 260)
#---------------------------TREE SCROLL BAR ---------------------------------------------------#
        self.treeScroll = ttk.Scrollbar(master)
        self.treeScroll.configure(command=self.tree.yview)
        self.tree.configure(yscrollcommand = self.treeScroll.set)
        self.treeScroll.pack(side= RIGHT, fill= BOTH)
        self.tree.place(x=10, y = 260)

        self.ADDjob_to_tree_view_refresh()


    def Show_More_Information(self):
        selected_item3 = self.tree.focus()
        item_details2 = self.tree.item(selected_item3)
        placeholder1 = item_details2.get("values")
        showinfo(title='Information', message=(placeholder1[0]))
        
     
        
         
    def ADDjob_to_tree_view_refresh(self):
        
 #----------------------------------------------------------------GRABS THE MAXIMUM VALUE AND DELETES ANY PREVIOUS VALUES IN THE TABLE -----------------------------#       
        try:
            self.Delete_all_jobs()
            cursor.execute("SELECT MAX(jobID) FROM AddJob") 
            jobID = cursor.fetchall()
            for x in jobID:
               jobID_value = (x[0]+1)
               
 #-----------------------------------------------------------------ADDS ALL THE CURRENT VALUES IN THE ADD TABLE WITH THE NEW MAXMIUM VALUE-----#       
            for i in range (1,jobID_value):
              
              cursor.execute('SELECT jobtitle,jobdescription,Name,JobPay,JobPrevious,JOBHOURS,jobID FROM AddJob WHERE jobID =(?)',(i,)) 
              conn.commit()
              value = cursor.fetchall()
              for row in value:
                      self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],))
        except:
            pass
        
#------------------------------------------- CLOSE PAGE BUTTON METHOD ----------------------------------------------------------------------------------------------------#
    def ConfirmExit(self):
            
            
        ConfirmExit = tkinter.messagebox.askyesno("SCOPE CLIENT","ARE YOU SURE YOU WANT TO CLOSE THIS PAGE ")
        if ConfirmExit > 0:
            self.master.destroy()
            return
#--------------------------APPLY FOR JOB METHOD---------------------------------------------------------------------------------------------------#                               
    def apply_for_jobs(self):
        #----------------------------------------------- ALLOWS VALUE BEING SELECTED TO BE ASSIGNED TO VARIABLE-------#
        selected_item2 = self.tree.focus()
        item_details = self.tree.item(selected_item2)
        placeholder = item_details.get("values")
        jobID = placeholder[5]
        #------------------------------checks the login ID OF USER WHRRE THE JOB ID IS EQUAL TO THE ONE JUST FOUND FROM ABOVE --------------------------------------#
        cursor.execute('SELECT LoginID FROM AddJob WHERE jobID =(?)',(jobID,)) 
        conn.commit()
        PlaceHolder2 = cursor.fetchone()
        LoginID_OWNER_JOB = PlaceHolder2[0]
        #--------------------------------------------GETS THE PUBLIC USERID AND STORES IN VARIABLE---------------------------------------#
        LoginID_OFFER_JOB = UserIDSQL_GLOBAL
        #-----------------------------------------------------CHECKS IF THE CURRENT GLOBAL LOGIN ID is EQUAL TO THE current LOGIN ID OF THE OWNER OF THE JOB THEN YOU CANT APPLY TO THAT LISTING-------#
        if UserIDSQL_GLOBAL == LoginID_OWNER_JOB:
            self.Label = Label(self.master, text = """YOU CANT APPLY TO YOUR OWN LISTING """,font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
            self.Label.place(x=800,y=140)
       #-------------------------------------ELSE LETS THE APPLY TO THE JOB LISTING AND SAVES THE LOGINID OF THE USER AND THE JOB LISTING IN OFFER JOBS TABLE-----#     
        else:
            cursor.execute('INSERT INTO OfferJob VALUES (NULL,?,?,?)',(jobID,LoginID_OWNER_JOB,LoginID_OFFER_JOB))
            conn.commit()
        
          
    def View_offers(self):
        #------------------------CREATES A NEW GUI THAT ALLOWS YOU TO SEE YOUR OFFERS--------------#
        root4 = Toplevel(self.master)
        View_ALL_MY_OFFERS = View_all_offers(root4)

        
    def list_my_jobs(self):
        #----------------------------ONLY LISTS JOBS THAT THE USER HAS MADE------------#
        
        try:
            self.Delete_all_jobs()
            cursor.execute('SELECT jobtitle,jobdescription,Name,JobPay,JobPrevious,JOBHOURS,jobID FROM AddJob WHERE LoginID =(?)',(UserIDSQL_GLOBAL,)) 
            conn.commit()
            
            value = cursor.fetchall()
            
            for row in value:
               
               self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],))
        except:
            pass
        
    def Delete_all_jobs(self):
        #----------------------------DELETES ALL JOBS THAT ARE IN THE TABLE----------------------#
        try:
            for item in self.tree.get_children():
                self.tree.delete(item)
        except:
            pass
        
        
    def Delete_job(self):
        #-----------------------------DELETE JOB METHOD DELETES THE JOB FROM THE TREE VIEW TABLE ASWELL AS THE SQL TABLE---------#
        try:
            
           selected_item2 = self.tree.focus()
           item_details = self.tree.item(selected_item2)
           placeholder = item_details.get("values")
           jobID = placeholder[5]
           cursor.execute('SELECT LoginID from AddJob WHERE jobID =(?)',(jobID,))
           conn.commit()
           value2 = cursor.fetchone()
           LOGINID_FROM_JOBOWNER = value2[0]
           
           cursor.execute('SELECT UserAdmin from UserInfo WHERE userID=(?)',(UserIDSQL_GLOBAL,))
           conn.commit()
           value4 = cursor.fetchone()
           Is_admin = value4[0]
           
           
           
           
           if LOGINID_FROM_JOBOWNER == UserIDSQL_GLOBAL or Is_admin == "True":
               
               try:
                   
                   selected_item = self.tree.selection()[0]
        
    
                   cursor.execute('DELETE FROM AddJob WHERE jobID =(?)',(jobID,))
                   conn.commit()
                   self.tree.delete(selected_item)
               except:
                    pass
               
           else:
               self.Label = Label(self.master, text = """THIS IS NOT YOUR JOB LISTING YOU CANT DELETE THIS """,font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
               self.Label.place(x=750,y=160)
        except:
            pass
           
        
    def filter_button(self):
        #----------------------GRABS FILTER CHOICE THEN CHECKS THE FILTER CHOICE IN THE SQL TABLE AND BRINGS BACK THE VALUES THAT MATCH THE QUICK FILTERING-----#
        dropdown1 = self.filterchoice.get()
        
        if dropdown1 == "Quick Filter":
            pass
        else:
            try:
                dropdown1 = "%" + dropdown1+ "%"
                self.Delete_all_jobs()
                cursor.execute('SELECT jobtitle,jobdescription,Name,JobPay,JobPrevious,JOBHOURS,jobID FROM AddJob WHERE jobtitle like(?)',(dropdown1,)) 
                conn.commit()
                value = cursor.fetchall()
            
                for row in value:
                   self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],))
            except:
                pass
            
            
            
            
            
            
        
    def Search_for_Button(self):
        #--------------------------------------GRABS THE VALUE FROM THE SEARCH BAR AND THEN FINDS ANY VALUES THAT MATCH AND BRINGS THEM BACK INTO THE TREEVIEW----#
        search_item = self.searchinput.get()
        if  search_item == "":
            pass
        else:
            self.Delete_all_jobs()
            search_item = "%"+search_item +"%"
            cursor.execute('SELECT jobtitle,jobdescription,Name,JobPay,JobPrevious,JOBHOURS,jobID FROM AddJob WHERE jobtitle like (?) OR JobPay like (?) OR Name like (?)',(search_item.lower(),search_item,search_item.lower())) 
            conn.commit()
            value = cursor.fetchall()
            for row in value:
                self.tree.insert("",0,text=row[0], values=(row[1],row[2],row[3],row[4],row[5],row[6],))
            
            
        
        
    def Add_job(self):
        #------------------- ALLOWS FOR A NEW GUI TO ADD NEW JOBS---------#
        root3 = Toplevel(self.master)
        ADD_JOBGUI = ADD_JOB(root3)

        
class ADD_JOB():
    
     def __init__(self, master):

        self.master = master
        self.master.title("Add Job")
        self.master.config(bg="CadetBlue1")
        self.master.geometry("400x500")
        #-------------------------------MAIN TITLE-------------------------------------------------------------------------------------
        self.title = Label(self.master,text = "SCOPE ADD JOB PAGE",bg="CadetBlue1",font = ("Ariel", 20, "bold"))   #names the Large Title above the page                                                                                       # puts it onto the page
        self.title.place(x=50,y=20)
        #places the coordinates 
        self.addjobtitle = Label(self.master,text = "Enter your job details to be listed :",bg="CadetBlue1",font=("Ariel", 13, "bold"))    # creates title to state where to put in details                                                                                 # puts this onto the screen
        self.addjobtitle.place(x=55,y=90)
        
        #----------------------SUB TITLE----------------
        self.display = Label(self.master,text = "ALL this information will be public to see",bg="CadetBlue1",font = ("Ariel", 10, "bold"))   #names the Large Title above the page                                                                                      # puts it onto the page
        self.display.place(x=50,y=150)
        #---------------------------NAME ENTRY----------------------------#
        self.job_Name = Label(self.master,text = "Name:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.job_Name.place(x=100,y=200)
        
        self.Job_Name_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_Name_entry.place(x=160,y=200)
        #------------------------------------JOB TITLE ENTRY----------------------------------------------------#

        self.job_title = Label(self.master,text = "Job Title:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.job_title.place(x=90,y=230)
        
        self.Job_title_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_title_entry.place(x=160,y=230)
        #------------------------------------------JOB DESCRIPTION--------------------------------------------------------------#
        self.job_description = Label(self.master,text = "Job Description:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.job_description.place(x=50,y=260)
        
        self.Job_description_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_description_entry.place(x=160,y=260)
        #------------------------------------------------------EXPECTED PAY----------------------------------------------------------------#
        self.job_pay = Label(self.master,text = "Expected rates for Job:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.job_pay.place(x=1,y=290)
        
        self.Job_pay_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_pay_entry.place(x=160,y=290)
        #--------------------------------------------PREVIOUS JOB TITLE--------------------------------------------------------------------#
        self.job_Previous = Label(self.master,text = "Previous job title:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.job_Previous.place(x=30,y=320)
        
        self.Job_Previous_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_Previous_entry.place(x=160,y=320)
        #-----------------------------------------------JOB HOURS -----------------------------------------#
       
        self.Job_hours = Label(self.master,text = "Expected hours:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.Job_hours.place(x=30,y=350)
        
        self.Job_hours_entry = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Job_hours_entry.place(x=160,y=350)
        
        #-------------------------------QUIT APPLICATION ------------------------------------------
        
        self.quits_button = Button(master, text = 'Quit Application ', command = self.ConfirmExit)
        self.quits_button.place(x=250,y=460)

        #-------------------------------------ADD JOB BUTTON-----------------------------------------------------------------------#

        self.addjob_button = Button(master, text = 'ADD JOB ', command = self.add_job_details_sql)
        self.addjob_button.place(x=180,y=460)
        #------------------------------------------------------------------------------------------------------------------------#

     def add_job_details_sql(self):
         #--------------------------------GRABS ALL THE JOB DETAILS ------------------------------------------------------------------------------------------ 
         userID = UserIDSQL_GLOBAL
         name =self.Job_Name_entry.get()
         title =self.Job_title_entry.get()
         
         description = self.Job_description_entry.get()
         pay = self.Job_pay_entry.get()
         previous = self.Job_Previous_entry.get()
         hours = self.Job_hours_entry.get()
         #--------------------------------IF THE PREVIOUS JOB IS LEFT EMPTY LEAVES N/A------------------------------------------------------------------------------------------ 
         if previous ==  "":
             previous = "N/A"
         #--------------------------------------LEAVES AN ERROR IF BOXES LEFT EMPTY------------------------------------------------------------------------------------ 
         if name == "" or title == "" or description == "" or pay == "" or previous == "" or hours == "": 
          self.empty_box_label = Label(self.master, text = """Dont leave Entry boxes Empty""",font  = ("Ariel", 10, "bold"),foreground = "red",bg="CadetBlue1")
          self.empty_box_label.place(x=70,y=400)
         #----------------------------------------ADDS JOB VALUES INTO THE ADD JOB TABLE ALL AS LOWER CASE VALUES---------#
         else:
             cursor.execute('INSERT INTO AddJob VALUES (NULL,?,?,?,?,?,?,?)',(title.lower(),description,name.lower(),previous,pay,hours,userID))
             conn.commit()
             self.master.destroy()
             
#-------------------------------------EXIT MTHOD-------------------------------
        
     def ConfirmExit(self):
        ConfirmExit = tkinter.messagebox.askyesno("SCOPE CLIENT","ARE YOU SURE YOU WANT TO CLOSE THIS PAGE ")
        if ConfirmExit > 0:
            self.master.destroy()
            return
    
        
class View_all_offers():
    #-------------------------------------CONSTRUCTOR-----------------------#
    
    def __init__(self, master):
        self.master = master
        self.master.title("View Offers")
        self.master.config(bg="CadetBlue1")
        self.master.geometry("1000x500")
        self.current_LOGINID = UserIDSQL_GLOBAL

        #---------------------------------------------------LABELING THE PAGE ---------------------------------------------------------------------------------------------------
        self.title = Label(self.master,text = "SCOPE VIEW OFFERS PAGE",bg="CadetBlue1",font = ("Ariel", 20, "bold"))   #names the Large Title above the page                                                                                       # puts it onto the page
        self.title.place(x=350,y=20)
        #--------------------------------------------------------BUTTON TO QUIT --------------------------------------------------------------------------------------------
        self.quit_button = Button(master, text = 'Quit Application ', command = self.ConfirmExit)
        self.quit_button.place(x=750,y=60)
        
        self.file_name = Label(self.master,text = "File name:",bg="CadetBlue1",font = ("Ariel", 10, "bold"))                                                                                    # puts it onto the page
        self.file_name.place(x=230,y=60)
        
        self.Name_of_file = Entry(master,bd =3, width=17, font=('Arial 10'))
        self.Name_of_file.place(x=310,y=60)

        
        self.make_file_button = Button(master, text = 'Insert Offer information into text file', command = self.MakeFile)
        self.make_file_button.place(x=450,y=60)
        #-----------------------------------------CREATES THE STYLE OF THE TREEVIEW -----------------------------------------------------------------------------------------------------------
        self.style2 = ttk.Style()
        self.style2.theme_use("alt")
        self.style2.configure("Treeview", background ="silver",foreground = "black", rowheight= 35, fieldbackground="silver" )
        self.style2.map("Treeview",background=[("selected","light green")])
        self.tree1 = ttk.Treeview(master,)
       
        self.tree1["columns"] = ("0", "1", "2")

        #------------------------------------------------ Set the column headers-----------------------------#
        self.tree1.heading("#0", text="My Job Lisiting ")
        self.tree1.heading("#1", text="Username of user offering")
        self.tree1.heading("#2", text="Name")
        self.tree1.heading("#3", text="Contact information of User offering")
       
      #----------------------------------------------ADDS SCROOLL BAR ONTO THE TREE VIEW-----------------------------------------#
        self.tree1.place(x=10, y = 100)

        self.treeScroll = ttk.Scrollbar(master)
        self.treeScroll.configure(command=self.tree1.yview)
        self.tree1.configure(yscrollcommand = self.treeScroll.set)
        self.treeScroll.pack(side= RIGHT, fill= BOTH)
        self.tree1.place(x=10, y = 100)
        
        
    #--------------------------------------------------SELECTS ALL VALUES NEEDED AND THEN ADDS THEM TO THE TREE VIEW--------#
        try:
            try:
                cursor.execute("SELECT MAX(OfferID) FROM OfferJob WHERE LoginID_OWNER_JOB =(?)",(self.current_LOGINID,))
                conn.commit()
                maxnumber = cursor.fetchall()
                for x in maxnumber:
                   maxofferID = (x[0]+1)
            except:
                pass
                
            self.arrayofOfferinfo =[]
            current_users_job_ID = ""
            for i in range(0,maxofferID):

                cursor.execute('SELECT OfferJob.jobID,OfferJob.LoginID_OFFER_JOB,AddJob.jobtitle FROM OfferJob LEFT JOIN AddJob ON OfferJob.JobID = AddJob.jobID  WHERE OfferJob.LoginID_OWNER_JOB = (?) ',(self.current_LOGINID,)) 
                conn.commit()
                values_from_offerjob = cursor.fetchall()
                current_users_job_ID = values_from_offerjob[i][0]
                login_ID_FROM_OFFER = values_from_offerjob[i][1]
                self.jobtitle = values_from_offerjob[i][2]
        
                cursor.execute('SELECT Userinfo.email,Login.username,Userinfo.name FROM UserInfo LEFT JOIN Login ON Userinfo.userID = Login.LoginID WHERE Userinfo.userID = (?)',(login_ID_FROM_OFFER,)) 
                conn.commit()
                email_username_name = cursor.fetchone()
                self.email = email_username_name[0]
                self.usernames = email_username_name[1]
                self.name = email_username_name[2]
                self.tree1.insert("",0,text = self.jobtitle, values=(self.usernames,self.name,self.email))

                list1 = (self.jobtitle+" ",self.usernames+" ",self.name+" ",self.email+" "+"\n")
                self.arrayofOfferinfo.append(list1)
               
               
              
                
     #---------------------------------IF NO ONE HAS APPLIED TO THE JOB THEN NO JOB OFFERS ARE FOUND 

        except:
            if current_users_job_ID == "":
                
                self.no_offers = Label(self.master,text = "NO JOB OFFERS ",bg="CadetBlue1",font = ("Ariel", 10, "bold"),foreground = "red")   #names the Large Title above the page                                                                                       # puts it onto the page
                self.no_offers.place(x=100,y=60)
            
     
            
        


#------------------------EXIT METHOD ------------------------------------------------------------------------------------------------------#
        
    def ConfirmExit(self):
        ConfirmExit = tkinter.messagebox.askyesno("SCOPE CLIENT","ARE YOU SURE YOU WANT TO CLOSE THIS PAGE ")
        if ConfirmExit > 0:
            self.master.destroy()
            return

    def MakeFile(self):
        name = self.Name_of_file.get() + ".txt"
        file = open(name,"w")
        for i in range (0,len(self.arrayofOfferinfo)):
            file.writelines(self.arrayofOfferinfo[i])
        file.close
     
        

#--------------------------------------------------------------------------------------------------------------------------------#
        

        

def main():
    root = Tk()
    app = window(root)
    root.mainloop()
if __name__ == "__main__":
    main()
