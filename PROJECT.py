import pandas as pd
import time
import matplotlib.pyplot as plt

csv_file = "C:/Users/AmolNS/Desktop/ufc fighters.csv"

print("")
print("")
print("   Informatics Practices Project")
print('_'*35)
print("")
print("Made By: \n")
print("Amol NS, Aaryan Shetty, Andrew Aji Mathew")

time.sleep(2)

def clear():
    for x in range(5):
               print()

def main_menu():
           clear()
          
           
           while True:
                      print('\n            MAIN MENU ')
                      print('_'*40)
                      print()
                      print('1. Data Analysis Menu\n')
                      print('2. Graph Menu\n')
                      print('3. Export Menu\n')
                      print('4. Exit\n')
                      choice = int(input('Enter your choice :'))

        
                      if choice==1:
                                 
                                 data_analysis_menu()
                                 

                      if choice==2:
                                 graph()
                                   
        
                      if choice==3:
                                 export_menu()
                                    
        
                      if choice==4:
                                 break
           clear()
               
def data_analysis_menu():
        df = pd.read_csv(csv_file)   
        while True:
            clear()
            print('\n            Data Analysis Menu ')
            print('_'*40)
            print('1.  Show Whole DataFrame\n')
            print('2.  Insert a New Record\n')
            print('3.  Show Columns\n')
            print('4.  Show Top Rows\n')
            print('5.  Show Bottom Rows\n')
            print('6.  Show Specific Column\n')
            print('7.  Exit (Move to main menu)\n')
            ch = int(input('Enter your choice:'))
            print("")
            if ch == 1:
                print(df)
                print("")
                wait = input('Press any key to continue:')
                print("")
            if ch == 2:
                a = input('Enter FighterID :')
                b = input('Enter Name of Fighter :')
                c = input('Enter Fighter Nickname :')
                d = input('Enter Weightclass :')
                data={'fid':a,'name':b,'nickname':c,'class':d}
                df = df.append(data,ignore_index=True)
                print(df)
                wait = input('Press any key to continue:')
                print("")

            if ch == 3:
                print(df.columns.tolist())
                print("")
                wait = input('Press any key to continue:')
                print("")
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                print("")
                wait = input('Press any key to continue:')
                print("")
            if ch == 5:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                print("")
                wait = input('Press any key to continue:')
                print("")
            if ch == 6:
                print(df.columns)
                print("")
                col_name = input('Enter the column you want to print : ')
                print("")
                print(df[col_name])
                print("")
                wait = input('Press any key to continue:')
                print("")   
            if ch == 7:
                break

def graph():
    df = pd.read_csv(csv_file)
    df1=df.head(10)
    while True:
        clear()
        print('\n            GRAPH MENU ')
        print('_'*40)
        print('\n1.  Line Graph \n')
        print('2.  Bar Graph \n')
        print('3.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:' ))
        
        if ch==1:
            a = df.pivot_table(index=['class'], aggfunc='size')
            b = a.reset_index(name='weight')
            plt.plot(b['class'],b['weight'])
            plt.xticks(rotation=45)
            plt.ylabel("Number of Fighters")
            plt.xlabel('Weight Class',fontsize=3)
            plt.title('Fighters in each Weight Class')
            plt.show()
            
        if ch==2: 
            a = df.pivot_table(index=['class'], aggfunc='size')
            b = a.reset_index(name='weight')
            plt.bar(b['class'],b['weight'])
            plt.xticks(rotation=45)
            plt.ylabel("Number of Fighters")
            plt.xlabel('Weight Class',fontsize=3)
            plt.title('Fighters in each Weight Class')
            plt.show()
                   

        if ch==3:
            break

def export_menu():   
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n            EXPORT MENU ')
        print('_'*40)
        print()
        print('1.  CSV File\n')
        print('2.  Exit (Move to main menu)')
        print("")
        ch = int(input('Enter your Choice : '))
        
        if ch==1:
            df.to_csv('C:/Users/AmolNS/Desktop/ufc fighters_new.csv')
            print('\n The CSV file "mma_fighters_new.csv" has been saved on your Desktop')
            print("")
            wait = input('Press any key to continue:')
            print("")

        
        if ch == 2:
            break



           

main_menu()
        

