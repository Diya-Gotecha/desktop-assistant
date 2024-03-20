from tkinter.tix import IMAGETEXT


def cam():
    import tkinter
    from tkinter import messagebox
    import cv2
    import PIL.Image , PIL.ImageTk
    import time
    from cv2 import CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH
    from tkinter import Tk, Image
    from PIL import Image



    class App:
        def __init__(self, window, window_title,video_source=0):
            self.window=window
            self.window.title = (window_title)
            self.video_source = video_source

            def MyVideoCapture(self,video_source,window_title):
                  self.vid 
                  self.canvas = tkinter.Canvas(window , height=self.vid.height, width=self.vid.width)
                  self.canvas.pack()

                  btn_frame=tkinter.Frame(window,background="black")
                  btn_frame.place(x=0,y=0)

                  self.btn_snapshot=tkinter.Button(btn_frame ,text="Snapshot",command=self.snapshot,width=20,bg="black",fg="white")
                  self.btn_snapshot.pack(side= "left",padx=10,pady=10)

                  self.delay = 15
                  self.update()
        
                  self.window.mainloop()

        def snapshot(self):
             ret,frame=self.vid.get_frame()
             if ret:
                 cv2.imwrite("My Capture"+time.strftime("%d-%m-%Y-%H-%M-%S")+".jpg",cv2.cvtColor(frame, cv2.VideoCapture.get(cv2.CAP_PROP_FOURCC)))

                 messagebox.showinfo("Notifaction","Image Saved")

        def update(self):
             ret, frame=self.vid.get_frame()

             if ret:
                 self.photo = PIL.Image.Tk.PhotoImage(image=PIL.image.fromarray(frame))
                 self.photo = IMAGETEXT.PhotoImage(image=PIL.Image.fromarray(frame))

                 self.canvas.create_image(0,0,image=self.photo,anchor=tkinter.NW)
                 self.window.after(self.delay,self.update)


             
    
    class MyVideoCapture:
        def __init__(self, window, window_title,video_source=0):
            self.vid=cv2.VideoCapture(video_source)
            if not self.vid.isOpened():
                raise ValueError("unable to open video source",video_source)
            
            self.width = self.new_method()
            self.height= self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        def new_method(self):
            return self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)

        def get_frame(self):
            if self.vid.isOpened():
                 ret, frame= self.vid.read()
                 if ret:
                    return(ret, self.vid.get(cv2.CAP_PROP_FOURCC))

                 else:
                     return(ret,None)
                 
            else:
                return(ret,None)
            
    App(tkinter.Tk(),"Camera")
    
cam()
            
           