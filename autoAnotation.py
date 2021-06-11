#!/usr/bin/env python
#-*- coding:utf-8 -*-

#210603
#신호등 클래스 자동 분류 프로그램
#by minkyu
import cv2
import os

rootpath=os.path.dirname(os.path.realpath(__file__))
dirs=os.listdir(rootpath)
    



for dirname in dirs:
    dirpath=rootpath+'/'+dirname
    if os.path.isfile(dirpath):
        continue

    files=os.listdir(dirpath)
    files.sort()
    for filename in files:
        filepath=dirpath+'/'+filename

        print(filename)
        if filename.endswith("txt"):
            f=open(filepath,'r+')
            
            #print(filename)
            lines=[]

            fj=filename
            fj=fj.replace('txt','jpg')


            for line in f:
                if line ==  '\n':
                    continue


                words = line.split(' ')
                myclass = int(words[0])
                centerx=float(words[1])
                centery=float(words[2])
                width=float(words[3])
                height=float(words[4])

                if int(myclass) == 0 :
                    img=cv2.imread(fj,1)
                    h,w,c=img.shape
                    RW=width*w
                    RH=height*h
                    RCX=int(centerx*w)
                    RCY=int(centery*h)

                    RW8=int(RW/8)
                    


                    obj_img=img[int(RCY-RH/2):int(RCY+RH/2),int(RCX-RW/2):int(RCX+RW/2)].copy()
                    
                    #cv2.imshow("test",obj_img)
                    #cv2.waitKey()

                    hsv_img = cv2.cvtColor(obj_img,cv2.COLOR_BGR2HSV)
                    h,s,v = cv2.split(hsv_img)
                    ret, thrS = cv2.threshold(s, 170, 255, cv2.THRESH_BINARY)
                    thrSR = cv2.resize(thrS,(int(RW*4),int(RH*4)),cv2.INTER_CUBIC)
                    ret, thrV = cv2.threshold(v, 170, 255, cv2.THRESH_BINARY)
                    thrVR = cv2.resize(thrV,(int(RW*4),int(RH*4)),cv2.INTER_CUBIC)

                    l1 = 0
                    l2 = 0
                    l3 = 0
                    l4 = 0

                    for i in range(0,int(RH/3)) :
                        for j in range(0,int(RW/8)) :
                            l1 += thrV[int(RH/3)+i,int(RW/16)+j]
                            l2 += thrV[int(RH/3)+i,int(RW*5/16)+j]
                            l3 += thrV[int(RH/3)+i,int(RW*9/16)+j]
                            l4 += thrV[int(RH/3)+i,int(RW*13/16)+j]
                    print(l1,l2,l3,l4)
                    lm = 5*255                    
                    #cv2.imshow("test1",thrS)
                    cv2.imshow("test",thrVR)
                    
                    cv2.waitKey()
                    
                    # for i in range(0,3):
                    #     for j in range(0,3):
                            
                    if l1>lm and l3<lm :
                        myclass = 1
                        print(filename,"-",line,"change to 1")
                    elif l3>lm and l1>lm :
                        myclass = 2
                        print(filename,"-",line,"change to 2")
                    elif l2>lm :
                        myclass = 3
                        print(filename,"-",line,"change to 3")
                        
                    elif l4>lm and l3>lm :
                        myclass =4
                        print(filename,"-",line,"change to 4")
                    elif l4>lm and l3<lm :
                        myclass =5   
                        print(filename,"-",line,"change to 5")
                    else :
                        myclass =0
                        print(filename,"-",line,"change to 0")


           
                    line = "%d %s %s %s %s" % (myclass, centerx, centery, width, height)
                    lines+=line
            




            f.close()
            #print(lines)
            os.remove(filepath)
            f=open(filepath,'w')
            f.writelines(lines)




