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
                    img=cv2.imread(fj,0)
                    h,w=img.shape
                    RW=width*w
                    RH=height*h
                    RCX=int(centerx*w)
                    RCY=int(centery*h)

                    RW8=int(RW/8)
                    
                    l1 = 0
                    l2 = 0
                    l3 = 0
                    l4 = 0


                    l1=l1+img[RCY,RCX-RW8*3]+img[RCY-1,RCX-RW8*3]+img[RCY+1,RCX-RW8*3]+img[RCY,RCX-RW8*3-1]+img[RCY,RCX-RW8*3+1]
                    l2=l2+img[RCY,RCX-RW8]+img[RCY-1,RCX-RW8]+img[RCY+1,RCX-RW8]+img[RCY,RCX-RW8-1]+img[RCY,RCX-RW8+1]
                    l3=l3+img[RCY,RCX+RW8]+img[RCY-1,RCX+RW8]+img[RCY+1,RCX-RW8]+img[RCY,RCX-RW8-1]+img[RCY,RCX-RW8+1]
                    l4=l4+img[RCY,RCX+RW8*3]+img[RCY-1,RCX+RW8*3]+img[RCY+1,RCX+RW8*3]+img[RCY,RCX+RW8*3-1]+img[RCY,RCX+RW8*3+1]
                    
                    lm = (l1+l2+l3+l4)/4
                    
                    if l1>lm and l3<lm :
                        myclass = 1
                    elif l3>lm and l1>lm :
                        myclass = 2

                    elif l2>lm :
                        myclass = 3

                    elif l4>lm and l3<lm :
                        myclass =4
                    elif l4>lm and l3>lm :
                        myclass =5   
                    else :
                        myclass =0


           
                    line = "%d %s %s %s %s" % (myclass, centerx, centery, width, height)
                    lines+=line
            




            f.close()
            #print(lines)
            os.remove(filepath)
            f=open(filepath,'w')
            f.writelines(lines)




