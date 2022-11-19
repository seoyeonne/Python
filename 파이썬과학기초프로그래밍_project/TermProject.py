import tkinter as tk
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

window=tk.Tk()
window.title("infomation")
window.geometry("800x400+200+200")
window.resizable(True,True)

def save(): #입력완료
    print("이름:",name.get(),"\n")
    print("나이:",age.get(),"\n")
    print("학번:",number.get(),"\n")
    print("학년:",grade.get(),"\n")
    print("전공:",major.get(),"\n")
    print("email:",email.get(),"\n")
    print("1학년:",one.get(),"\n")
    print("2학년:",two.get(),"\n")
    print("3학년:",three.get(),"\n")
    print("4학년:",four.get())

def save_txt(): #파일에 저장 
    infofile=open("/Users/hwangseoyeon/Desktop/20205279_황서연.txt","w")
    infofile.write("이름:")
    infofile.write(name.get())
    infofile.write("\n나이:")
    infofile.write(age.get())
    infofile.write("\n학번:")
    infofile.write(number.get())
    infofile.write("\n학년:")
    infofile.write(grade.get())
    infofile.write("\n전공:")
    infofile.write(major.get())
    infofile.write("\nemail:")
    infofile.write(email.get())
    infofile.write("\n1학년:")
    infofile.write(one.get())
    infofile.write("\n2학년:")
    infofile.write(two.get())
    infofile.write("\n3학년:")
    infofile.write(three.get())
    infofile.write("\n4학년:")
    infofile.write(four.get())
    infofile.close()
    
def print_txt(): #파일내용출력
    infile=open("/Users/hwangseoyeon/Desktop/20205279_황서연.txt","r")
    line=infile.read()
    print(line)

def Image_Processing(): #이미지 출력
    image_1=tk.PhotoImage(file='/Users/hwangseoyeon/Desktop/Pic1.png')
    labelimage=tk.Label(window,image=image_1)
    labelimage.img = image_1
    labelimage.place(x=330,y=50)
    #labelimage.config(image=image_1)
    image_2=tk.PhotoImage(file='/Users/hwangseoyeon/Desktop/Pic2.png')
    labelimage=tk.Label(window,image=image_2)
    labelimage.img = image_2
    labelimage.place(x=320,y=150)
    

def RC_Circuit(): 
    Ydat = []
    Xdat = []
    Ndat=[]
    n_max=6000
#=== System Parameter of R-C Circuit =================
    R=100000 #Resistance
    C=0.000001 #Capacitance
    dt=0.00001 #Sampling period
#=== Initial Output ===================================
    Xtemp=0
    Ytemp=0
    Xdat.append(Ytemp)
    Ydat.append(Ytemp)
    num=dt/R/C
    for n in range (0,n_max):
        Xtemp=1 #Input 
        Ytemp1=Ytemp #Current Output
        Ytemp=(1-num)*Ytemp1+num*Xtemp #System Output Equation : Next Output
        Xdat.append(n*dt)
        Ydat.append(Ytemp)
        Ndat.append(n)
    fig = plt.figure()

    plt.plot(Xdat,Ydat)
    plt.xlabel('Time(sec)')
    plt.ylabel('Vc', fontsize=20)
    plt.title("Step Response")
    plt.grid(True)
    w = tk.Canvas(window)
    plt.show(window)
    
    

 
    
    

    
#개인정보
Label=tk.Label(window,text="개인 정보")
Label.grid(row=0,column=0)
#성명 
Label1=tk.Label(window,text="성명")
Label1.grid(row=1,column=0)
name=tk.Entry(window)
name.grid(row=1,column=1)
#나이
Label2=tk.Label(window,text="나이")
Label2.grid(row=2,column=0)
age=tk.Entry(window)
age.grid(row=2,column=1)
#학번
Label3=tk.Label(window,text="학번")
Label3.grid(row=3,column=0)
number=tk.Entry(window)
number.grid(row=3,column=1)
#학년
Label4=tk.Label(window,text="학년")
Label4.grid(row=4,column=0)
grade=tk.Entry(window)
grade.grid(row=4,column=1)

#전공
Label5=tk.Label(window,text="전공")
Label5.grid(row=5,column=0)
major=tk.Entry(window)
major.grid(row=5,column=1)
#email
Label6=tk.Label(window,text="email")
Label6.grid(row=6,column=0)
email=tk.Entry(window)
email.grid(row=6,column=1)

#학점 
Label_0=tk.Label(window,text="학점")
Label_0.grid(row=7,column=0)
#1학년
Label_1=tk.Label(window,text="1학년")
Label_1.grid(row=8,column=0)
one=tk.Entry(window)
one.grid(row=8,column=1)
#2학년
Label_2=tk.Label(window,text="2학년")
Label_2.grid(row=9,column=0)
two=tk.Entry(window)
two.grid(row=9,column=1)
#3학년
Label_3=tk.Label(window,text="3학년")
Label_3.grid(row=10,column=0)
three=tk.Entry(window)
three.grid(row=10,column=1)
#4학년
Label_4=tk.Label(window,text="4학년")
Label_4.grid(row=11,column=0)
four=tk.Entry(window)
four.grid(row=11,column=1)

#저장하고 textbox에 출력
button_1=tk.Button(window,text="입력완료",command=save)
button_1.grid(row=12,column=0)


#입력내용 파일에 저장
button_2=tk.Button(window,text="저장",command=save_txt)
button_2.grid(row=12,column=1)

#파일내용 출력
button_3=tk.Button(window,text="출력",command=print_txt)
button_3.grid(row=12,column=2)

#RC circuit
labelb1=tk.Label(window,text="RC circuit")
labelb1.grid(row=0,column=5)
button_4=tk.Button(window,text="RC circuit",command=RC_Circuit)
button_4.grid(row=12,column=3)

#Imageprcessing-이미지 출력
labelb2=tk.Label(window,text="Image Processing")
labelb2.grid(row=0,column=3)
button_5=tk.Button(window,text="Image Processing",command=Image_Processing)
button_5.grid(row=12,column=4)



window.mainloop()
