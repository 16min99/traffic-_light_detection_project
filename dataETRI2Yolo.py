import os


rootpath=os.path.dirname(os.path.realpath(__file__))
print(rootpath)
classnum=[1300,1301,1302,1303,1305,
          1400,1401,1402,1403,1404,1405,1406]


dirs = os.listdir(rootpath)
traintxt=open(rootpath+'/train.txt','w')
for _dir in dirs:
    if(os.path.isfile(_dir)):
        continue
    txtpath=rootpath+'/'+_dir+'/labels_class_5'
    imgpath=rootpath+'/'+_dir+'/JPEGImages_mosaic'

    txtfiles = os.listdir(txtpath)
    # print(directory)

    
    
    for file in txtfiles:
        txtfname=txtpath+'/'+file
        txtfile=open(txtfname,'r')
        read_txtfile=txtfile.read()
        lines=read_txtfile.split('\n')
        wrfile=0
        outputfname=imgpath+'/'+file
        if(read_txtfile==''):
            wrfile=1
        else:
          output=open(outputfname,'w')
          for line in lines:
              if(line==''):
                output.write(line)
              else:
                words = line.split('\t')
                
                left=float(words[0])
                top=float(words[1])
                right=float(words[2])
                bottom=float(words[3])
                myclass=(int)(words[4])

                if myclass in classnum:
                    for i in range(len(classnum)):
                        if(classnum[i]==myclass):
                            myclass=i
                            break
                else:
                    wrfile=1
                    break

                width=right-left
                height=bottom-top
                centerx=left+(width/2)
                centery=top+(height/2)
                width/=2048
                centerx/=2048
                height/=1536
                centery/=1536

                data = "%s %f %f %f %f\n" % (myclass, centerx,centery,width,height)
                output.write(data)

        imgfname=imgpath+'/'+file.replace("txt","jpg")
        if (wrfile==1):
            if(os.path.isfile(txtfname)):
                txtfile.close()
                os.remove(txtfname)
                print("rm text file")

            if(os.path.isfile(outputfname)):
                output.close()
                os.remove(outputfname)
                print("rm output file")
            
            if(os.path.isfile(imgfname)):
                os.remove(imgfname)
                print("rm img file")

        else:
            traindata="%s\n" % (imgfname)
            traintxt.write(traindata)
            print("parsing success ",imgfname)
