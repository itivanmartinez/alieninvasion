import graphics
import random
import math
import winsound
def spaceship():   
    #evaluates if bullets hit aliens
    score=0
    bullets=[]
    ufos=[]
    Shoot=""
    spcshipSpeed=10
    timeshowaliens=0
    #creates games' window
    win=graphics.GraphWin('Spaceship Invasion',800,600)
    #set true for loop
    continu="true"
    #draws score table
    score=0
    strscore=getScore()
    txtscoreRecord=graphics.Text(graphics.Point(80,80),strscore)
    txtscoreRecord.draw(win)
    txtinstrunctions=graphics.Text(graphics.Point(200,120),'Click to start Playing')
    txtinstrunctions.draw(win)
    txtscore=graphics.Text(graphics.Point(70,20),"Enter Your Name: ")
    txtscore.draw(win)
    nameinput=graphics.Entry(graphics.Point(250,20),25)
    nameinput.draw(win)
    x=graphics.GraphWin.getMouse(win)
    getname=nameinput.getText()
    nameinput.undraw()
    txtscoreRecord.undraw()
    txtinstrunctions.undraw()
    txt="Score:",score
    txtscore.setText(txt)
    #Creates first alien
    img=graphics.Image(graphics.Point(90, 550),"spaceship.png")
    img.draw(win)
    showaliensrdm=random.randint(1,10)
    #Controls for spaceship movement
    
    while continu=='true':
        #increase time for aliens attack when score is more than 10
        
            
        #checks keyboard
        string=win.checkKey()
        #moves spaceship to left
        imgpoint=img.getAnchor()
        imgpointx=imgpoint.getX()
        imgpointy=imgpoint.getY()
        if string=='Left':
            if imgpointx>60:
                img.move(-spcshipSpeed,0)
        #moves spaceship to right
        elif string=='Right':
            if imgpointx<740:
                img.move(spcshipSpeed,0)
        #Shoots bullets
        elif string=='space':
            if len(bullets)<5:                
                Shoot=Bullet(graphics.Point(imgpointx,imgpointy-60),graphics.Point(imgpointx,imgpointy-70))
                Shoot.setWidth(3)
                bullets.append(Shoot)
                Shoot.draw(win)
                #Plays shoot sound 
                winsound.PlaySound('shoot.wav', winsound.SND_ASYNC)
        #to quit game
        elif string=='q':
            message = graphics.Text(graphics.Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
            message.draw(win)
            continu="false"

        #Moves bullets if there are bullets shot
        if bullets:
            for i in bullets:
                i.move(0,-2)
                bulletsPoint=i.getP1()
                bulletsy=bulletsPoint.getY()
        #Deletes bullets when screen edge is reached
                if bulletsy<0:
                    i.undraw()
                    bullets.remove(i)
            cllsn=collision(bullets,ufos)
            score=score+int(cllsn)
            #updates score
            txt="Score:",score
            txtscore.setText(txt)
        #shows aliens
        if timeshowaliens==showaliensrdm:
            #shows maximun of 10 aliens at a time
            if len(ufos)<10:
                randomx=random.randint(60,740)
                randomy=random.randint(20,30)
                newufo=ufo(graphics.Point(randomx, randomy),"alienufo.png")
                newufo.draw(win)
                ufos.append(newufo)
                ufos[len(ufos)-1].speed=random.randint(1,2)
            if score<10:
                showaliensrdm=random.randint(300,400)
            elif score<15:
                showaliensrdm=random.randint(200,300)
            elif score<20:
                showaliensrdm=random.randint(150,200)
            else:
                showaliensrdm=random.randint(125,150)
            timeshowaliens=0           
        else:
            timeshowaliens=timeshowaliens+1
        #moves aliens if there are aliens
        if ufos:
            for x in ufos:
                #ufospeed=
                #print(ufospeed)
                x.move(0,x.speed)
                imgpoint=x.getAnchor()
                imgpointy=imgpoint.getY()
                #undraws ufos if screen edge is reached
                if imgpointy>560:
                    x.undraw()
                    ufos.remove(x)
                    score=score-1
                    txt="Score:",score
                    txtscore.setText(txt)
                    
        #Delays update of canvas           
        graphics.time.sleep(.008)
        win.update()
    writeScore(score,getname)
    win.getMouse()
    win.close()
#creates a class Bullet and inherits atributes from line
class Bullet(graphics.Line):
       pass
#creates ufo class. Inherits from image
class ufo(graphics.Image):
    pass
def collision(bllt,ufos):
    dx=0
    dy=0
    distance=0
    score=0
    if bllt and ufos:
        for i in bllt:    
            blltpoint=i.getP1()
            bllty=blltpoint.getY()
            blltx=blltpoint.getX()
            for x in ufos:
                ufospoint=x.getAnchor()
                ufosy=ufospoint.getY()
                ufosx=ufospoint.getX()
                dx=ufosx-blltx
                dy=ufosy-bllty
                distance=int(math.sqrt((dx*dx) + (dy*dy)))
                if distance<=x.getWidth()-12 and distance<x.getHeight()-30:                    
                    x.undraw()
                    ufos.remove(x)
                    i.undraw()
                    bllt.remove(i)
                    score=1
                    winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
    return score
def writeScore(score,name):
    #this function writes score and name to file
    counter=0
    file=open("scores.txt","r")
    for line in file:
        counter+=1
    file.close()
    if counter>4:
        file=open("scores.txt","r")
        lnscore=file.readlines()
        #removes first element from list
        lnscore.remove(lnscore[0])
        string=name+": "+str(score)+"\n"
        #adds string at end of list
        lnscore.append(string)
        file.close()
        #rewrites list on file
        file=open("scores.txt","w")
        for ln in lnscore:
            file.write(ln)
    else:
        file=open("scores.txt","a")
        string=name+": "+str(score)+"\n"
        file.write(string)
def getScore():
    #this function gets scores from file
    strToshow=""
    counter=0
    file=open("scores.txt","r")
    for line in file:
        strToshow+=line
    file.close()
    return strToshow        
spaceship()
