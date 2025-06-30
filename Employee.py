#Mysql
import mysql.connector
from datetime import date

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nani9003409417",
  database="employee_details"
)

mycursor=mydb.cursor()
mycursor.execute("DELETE FROM attendance")
mydb.commit()

#Pythonn
print("-----------Employee ERP------------")

user_input=int(input("Enter 1 to Log in or 2 to Sign up: "))
print("------------------------------------")

#Log in Function Used to log in the user!

def login():
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    if age>"18" or age<"100":
        pass
    else:
        print("Age Limit should be between 18 - 100 ")
        age=input("Enter age again: ")
    password = input("Enter password(Enter only in character): ")
    address=input("Enter address: ")
    mobile_number=input("Enter Mobile number: ")
    sql = "INSERT INTO employee (name,age,password,address,mobile_number)VALUE(%s,%s,%s,%s,%s)"
    val = (name, age, password,address,mobile_number)
    mycursor.execute(sql, val)

    mydb.commit()

    return password
#Display function used to display the Dashboard!
def display():
    print("------------------------------------")
    print("""Dashboard: 
             1)Employee Details
             2)Attendance
             3)Salary 
             4)Exit""")
    print("------------------------------------")
    print("""Enter 1 to view Employee details,
         2 to view Attendance,
         3 to view Salary,
         4 to Exit""")
    display_choice = int(input("Choice: "))
    return display_choice
#Employee details to access their detail and modify it
def employee_details():
    print("------------------------------------")
    print("""Dashboard:
             1)Employee Details
             2)Update Details
             3)Delete Employee
             4)Exit""")
    print("------------------------------------")
    print("""Enter 1 to view Employee Related
         2 to view Update Details
         3 to view Delete Employee
         4 to Exit""")
    b = int(input("Choice: "))
    print("------------------------------------")
    return b
#Employee persnol details
def employee_related():
    sql="SELECT name,age,password,address,mobile_number FROM employee WHERE name=%s"
    val=(name,)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    if myresult:
            print("EMPLOYEE DETAILS: ")
            print("Name:          ", myresult[0][0] )
            print("Age:           ", myresult[0][1])
            print("Password:      ",myresult[0][2])
            print("Address:       ",myresult[0][3])
            print("Mobile number: ",myresult[0][4])
#Update details
def update_detail():
    update_choice=int(input("""Enter 1 to update name,
            2 update age,
            3 update password,
            4 update address,
            5 mobile number: """))
    if update_choice==1:
        new_name = input("Enter your name to update: ")
        sql = "UPDATE employee SET name=%s WHERE name=%s "
        val = (new_name, name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Your name has been updated")
    elif update_choice==2:
        new_age = input("Enter your age to update: ")
        sql = "UPDATE employee SET age=%s WHERE name=%s "
        val = (new_age, name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Your age has been updated")
    elif update_choice==3:
        new_password = input("Enter your password to update: ")
        sql = "UPDATE employee SET password=%s WHERE name=%s "
        val = (new_password, name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Your password has been updated")
    elif update_choice==4:
        new_address=input("Enter your new address to update: ")
        sql="UPDATE employee SET address=%s WHERE name=%s "
        val=(password,name,)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Your address has been updated!!")
    elif update_choice==5:
        mobile_num = input("Enter your mobile number to update: ")
        sql = "UPDATE employee SET mobile_number=%s WHERE name=%s "
        val = (mobile_num, name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Your mobile number has been updated!!")
    else:
        print("Invalid Choice")
#DELETE employee details
def delete_details():
    delete_input=int(input("Enter 1 Delete Account :"))
    if(delete_input==1):
        sql="DELETE FROM employee WHERE name=%s"
        val=(name,)
        mycursor.execute(sql,val)
        mydb.commit()
        print("Your Account has been deleted successfully!")
#Attendance function -
def attendance():
    print("------------------------------------")
    print("""Mark Attendance for the day:
           1)Present
           2)Absent""")
    attendance_choice=int(input("Choice: "))
    print("------------------------------------")
    return attendance_choice
#Salary function - using total present
def salary():
    present_count = 0
    absent_count = 0
    mycursor.execute("SELECT Present FROM attendance ")
    myresult=mycursor.fetchall()
    for i in myresult:
        present_count+=1
    print("Total Days Present: ",present_count)
    mycursor.execute("SELECT Absent FROM attendance ")
    myresult_ab=mycursor.fetchall()
    for i in myresult_ab:
        absent_count+=1
    print("Total Days Absent: ",absent_count)
    print("------------------------------------")
    return present_count
#user_input 1 ,for log in
n=1
while n>0:
    if(user_input==1):
        login()
        print("You have Logged in Successfully!!")

        display_choice_a=display()
        n=True
        while n==True:
            if display_choice_a==1:
                print("------------------------------------")
                b=employee_details()
                if b == 1:
                    employee_related()
                elif b == 2:
                    update_detail()
                elif b == 3:
                    delete_details()
                else :
                    print("Invalid Choice")

                display_choice_a=display()
            elif display_choice_a==2:
                 attendance_choice=attendance()
                 mycursor.execute("SELECT Present,Absent,date FROM attendance ")
                 myresult = mycursor.fetchall()
                 if myresult:
                     print("------------------------------------")
                     print("Present: ", myresult[0][0],  "Date: ", myresult[0][2])
                     print("Absent: ",myresult[0][1],"Date: ",myresult[0][2])
                 if attendance_choice==1:
                     today=date.today()
                     sql="INSERT INTO attendance(Present,date)VALUES(%s,%s)"
                     val=(1,today)
                     mycursor.execute(sql,val)
                     mydb.commit()
                 else:
                     today=date.today()
                     sql = "INSERT INTO attendance(Absent,date)VALUES(%s,%s)"
                     val = (1, today)
                     mycursor.execute(sql, val)
                     mydb.commit()
                 display_choice_a = display()


            elif display_choice_a==3:
                tot_present_count=salary()
                salary=tot_present_count*750
                print("Salary: ",salary)
                display_choice_a = display()
                print("------------------------------------")

            elif display_choice_a==4:
                print("Thank you!")
                print("------------------------------------")
                n=False
                break
    #user_input 2 for sign in
    elif(user_input==2):
        name=input("Enter name: ")

        sql="SELECT*FROM employee WHERE name=%s "
        val=(name,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall()
        if(myresult):
            print("User already exits, Log in")
            name = input("Enter name: ")
            password=str(input("Enter password(Enter only in Characters): "))
            sql="SELECT password from employee WHERE name=%s"
            val=(name,)
            mycursor.execute(sql,val)
            myresult=mycursor.fetchall()
            for i in myresult[0]:
                if i==password:
                    print("You have logged in Successfully!")

                    display_choice_a = display()
                    n = True
                    while n == True:
                        if display_choice_a == 1:
                            b=employee_details()
                            if b==1:
                                employee_related()
                            elif b==2:
                                update_detail()
                            elif b==3:
                                delete_details()
                            else:
                                print("Invalid choice")



                            display_choice_a = display()
                        elif display_choice_a == 2:
                            attendance_choice = attendance()
                            mycursor.execute("SELECT Present,Absent,date FROM attendance ")
                            myresult = mycursor.fetchall()
                            if  myresult:
                                print("------------------------------------")
                                print("Present: ", myresult[0][0], "Date: ", myresult[0][2])
                                print("Absent: ", myresult[0][1], "Date: ", myresult[0][2])
                            if attendance_choice == 1:
                                today = date.today()
                                sql = "INSERT INTO attendance(Present,date)VALUES(%s,%s)"
                                val = (1, today)
                                mycursor.execute(sql, val)
                                mydb.commit()
                            else:
                                today = date.today()
                                sql = "INSERT INTO attendance(Absent,date)VALUES(%s,%s)"
                                val = (1, today)
                                mycursor.execute(sql, val)
                                mydb.commit()

                            display_choice_a = display()

                        elif display_choice_a == 3:
                            tot_present_count = salary()
                            salary = tot_present_count * 750
                            print("Salary: " , salary)
                            display_choice_a = display()
                            print("------------------------------------")
                        elif display_choice_a==4:
                            print("Thank you")
                            print("------------------------------------")
                            n = False
                            break

        else:
            print("User not exits")
            login()
            print("------------------------------------")

    else:
        print("Thank you,Come Again ")
        n=0
        break
