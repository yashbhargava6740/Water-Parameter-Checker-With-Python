# Importing Required Modules, Functions and methods
from csv import excel_tab
from PIL import Image
from statistics import mode
import cv2
from tkinter import Tk, Button, Toplevel, filedialog, Label, PhotoImage, mainloop
from pygame import mixer

# Backend Part
def counter(c):
    fptr = open("C_count.txt", "a+")
    fptr.seek(0)
    rd = fptr.readlines()
    if str(c) + "\n" not in rd:
        fptr.write(str(c))
        fptr.write("\n")
        fptr.close()
        return True
    else:
        #fptr.seek(0)
        fptr.close()
        return False


def mainData(filename,st):
    fptr = open("Main_Data.txt", "a+")
    st1 = f"{filename} --> {st}\n\n"
    fptr.write(st1)
    fptr.seek(0)
    fptr.close()

def playMusic():
    mixer.init()
    mixer.music.load("song.mp3")
    mixer.music.play()

def sample():
    try:
        window = Toplevel()
        window.geometry('640x640')
        window.title("Sample Images")
        window.minsize(640,640)
        window.maxsize(640,640)
        bg = PhotoImage(file = "bg1.png")
        label1 = Label(window, image = bg)
        label1.place(x = 0,y = 0)
        label = Label(window, text = 'Sample Images', font =('Verdana', 15))
        label.grid(column = 1, padx = 250)
        photo = PhotoImage(file = '2.png')
        btn1 = Button(window, text = 'Click Me !', image = photo, command = lambda : mainFun1('2.png'))
        btn1.grid(row = 4, column = 1, padx = 10, pady = 10)
        photo2 = PhotoImage(file = "4.png")
        btn2 = Button(window, text = 'Click Me !', image = photo2, command = lambda : mainFun1("4.png"))
        btn2.grid(row = 6, column = 1, padx = 10, pady = 10)
        photo3 = PhotoImage(file = "3.png")
        btn3 = Button(window, text = 'Click Me !', image = photo3, command = lambda : mainFun1("3.png"))
        btn3.grid(row = 8, column = 1, padx = 10, pady = 10)
        mainloop()
    except Exception as e :
        print(f"An error occured with error : {e}")

def mainFun1(filename):
    try:
        im = Image.open(filename)
        pix = list(im.getdata())
        n = len(pix)
        i = 0

            # Main Algorithm
        while(i < len(pix)):  # REMOVING WHITE PIXELS OR GRAY PIXELS
            p = pix[i]
            if(p[0] >= 140 and p[1] == p[2]):
                pix.pop()
            i += 1
        l = mode(pix)

            # Initializing Reoprts
        alg, mud, bacteria, fit = "NO", "LOW", "Probably low", "Fit"
        DO = "Normal"

        if(l[0] > l[1] and l[0] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
            if(l[0]-l[1] > 50):
                alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"]
            elif(l[0]-l[1] > 70 and l[0]-l[2] > 70):
                alg,mud,fit,DO, bacteria = ["Red", "High", "Not", "Not Good", "High"]
            if(l[0] > 100 and l[1] > 100):
                if(l[0]-l[1] > 50):
                    alg,mud,fit,DO, bacteria = ["Reddish Green", "High", "Not", "Not Good", "High"]
                elif(l[0]-l[1] > 10):
                    alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]
            elif(l[0] > 200 and l[1] > 200):
                alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Not Good", "High"]

        if(l[1] > l[0] and l[1] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
            if(l[0]-l[1] > 50):
                alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"] 
            elif(l[1]-l[1] > 70 and l[0]-l[2] > 70):
                alg,mud,fit,DO, bacteria = ["Green", "High", "Not", "Not Good", "High"]
                    
            if(l[0] > 100 and l[1] > 100):
                if(l[1]-l[2] > 50):
                    alg,mud,fit,DO, bacteria = ["Greenish Red", "High", "Not", "Not Good", "High"]
                elif(l[1]-l[2] > 10):
                    alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]       
            elif(l[0] > 200 and l[1] > 200):
                alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Average", "High"]
        print("Result:")
        print("*******")
        print("BACTERIA : ", bacteria, "\nAlgae content :", alg,"\nMud content : ", mud, "\nDissoved Oxygen Status : ", DO)
        print()
        print("********************************")
        print(f" Conclusion : {fit} for drinking ")
        print("********************************")
    except Exception as e:
        print(f"An Error occured with error : {e}")    

def close():
   #win.destroy()
   window.quit()

def browse():
    try:
        def select_file():
            filetypes = (
                ('JPEG file', '*.jpg'),
                ('GIF', '*.gif'),
                ('PNG', '*.png'),
                ('All files', '*.*')
            )

            filename = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes)
            mainFun1(filename)
        window = Tk()
        window.geometry('180x100')
        window.minsize(180, 100)
        window.maxsize(180, 100)
        window.title('File Explorer')
        window.config(background="Black")
        label_file_explorer = Label(window, text="Select Desired File", width=100, height=4, fg="blue")
        button_explore = Button(window,text="Browse Files",command=select_file)
        #button_explore.pack(side = 'top')
        button_explore.grid(row = 0, column = 1, padx = 55, pady = 10)
        button_exit = Button(window,text="Exit",command=close)
        #button_exit.pack(side = 'top')
        button_exit.grid(row = 1, column = 1, padx = 55, pady = 10)
        window.mainloop()
    except Exception as e:
        print(f"An error occured with error : {e}")

def mainFun():
    # Capturing Sample Image
    try:
        c = 0
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # CAP_DSHOW To avoid warnings
        cv2.namedWindow("test")
        img_name = ""
        while True:
            ret, frame = cam.read()
            if not ret:
                print("Technical Issue")
                break
            cv2.imshow("test", frame)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                print("Closed......")     # Exit on Escape
                break
            elif k % 256 == 32:
                while True:
                    out = counter(str(c))
                    if out:
                        img_name = f"opencv_frame_{str(c)}.jpg"    # Press Space To Capture
                        cv2.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        c += 1
                        break
                    c += 1
                break
        cam.release()
        im = Image.open(img_name)
        pix = list(im.getdata())
        n = len(pix)
        i = 0

        # Main Algorithm
        while(i < len(pix)):  # REMOVING WHITE PIXELS OR GRAY PIXELS
            p = pix[i]
            if(p[0] >= 140 and p[1] == p[2]):
                pix.pop()
            i += 1
        l = mode(pix)

        # Initializing Reoprts
        alg, mud, bacteria, fit = "NO", "LOW", "Probably low", "Fit"
        DO = "Normal"

        if(l[0] > l[1] and l[0] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
            if(l[0]-l[1] > 30):
                alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"]
            elif(l[0]-l[1] > 70 and l[0]-l[2] > 70):
                alg,mud,fit,DO, bacteria = ["Red", "High", "Not", "Not Good", "High"]
            if(l[0] > 100 and l[1] > 100):
                if(l[0]-l[1] > 30):
                    alg,mud,fit,DO, bacteria = ["Reddish Green", "High", "Not", "Not Good", "High"]
                elif(l[0]-l[1] > 10):
                    alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]
            elif(l[0] > 200 and l[1] > 200):
                alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Not Good", "High"]

        if(l[1] > l[0] and l[1] > l[2]):  # CHECKING FOR REDDISH GREEN OR BROWN ALGAE
            if(l[0]-l[1] > 50):
                alg,mud,fit,DO = ["No", "Filterable", "After Filtaration", "Probably Decent"] 
            elif(l[1]-l[1] > 70 and l[0]-l[2] > 70):
                alg,mud,fit,DO, bacteria = ["Green", "High", "Not", "Not Good", "High"]
                
            if(l[0] > 100 and l[1] > 100):
                if(l[1]-l[2] > 50):
                    alg,mud,fit,DO, bacteria = ["Greenish Red", "High", "Not", "Not Good", "High"]
                elif(l[1]-l[2] > 10):
                    alg,mud,fit,DO, bacteria = ["Greenish", "High", "Not", "Not Good", "High"]       
            elif(l[0] > 200 and l[1] > 200):
                alg,mud,fit,DO, bacteria = ["Probably Low and Reddish Green", "Low But Exists", "Not", "Average", "High"]
        
        st4 = f'''Bacteria : {bacteria}
                    \t\tAlgae content : {alg}
                    \t\tMud Content : {mud}
                    \t\tDissolved Oxygen Status : {DO}'''
        mainData(img_name, st4)
        print("Result:")
        print("*******")
        print("BACTERIA : ", bacteria, "\nAlgae content :", alg,"\nMud content : ", mud, "\nDissoved Oxygen Status : ", DO)
        print()
        print("********************************")
        print(f" Conclusion : {fit} for drinking ")
        print("********************************")
        #close()
    except Exception as e:
        print(f"Image not captured, Error : {e}")

'''Here Ends Backend Part'''

# User Interface
playMusic()
window = Tk()
window.geometry('260x180')  
window.minsize(260, 180)
window.maxsize(260, 180)
window.title('Water Parameters...')
bg = PhotoImage(file = "bg.png")
label1 = Label(window, image = bg)
label1.place(x = 0,y = 0)
btn = Button(window, text = 'Take a pic!',command = mainFun)
btn.grid(row = 0, column = 1, padx = 88, pady = 10)
btn1 = Button(window, text = 'Select Existing Pic', command = browse)
btn1.grid(row = 1, column = 1, padx = 88, pady = 20)
btn2 = Button(window, text = 'See Sample Pics', command = sample)
btn2.grid(row = 2, column = 1, padx = 88, pady = 15)
mainloop()