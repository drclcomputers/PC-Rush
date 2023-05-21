from ursina import *
app=Ursina()

window.color=color.black

viata=True
score=0.0
player=Entity(model="quad", texture="pers.png", scale=(0.8, 0.8), collider="box")

back=Audio("back.mp3", autoplay=True, loop=True)
sunet=Audio("sunet.mp3", autoplay=False, loop=False)

lose=Text(text="You lose! (Press 'r' to restart or 'q' to quit)", scale=3, color=color.red, position=(-0.72, 0.1))
lose.enabled=False

score1=Text(text=(str(score)), x=-0, y=0.5, scale=1, color=color.red)

perete1=Entity(model="quad", texture="perete24.png", position=(6, 4), scale=(1, 7.5), collider="box")
perete2=Entity(model="quad", texture="perete14.png", position=(6, -4), scale=(1, 4), collider="box")
perete3=Entity(model="quad", texture="perete14.png", position=(12, 4), scale=(1, 4), collider="box")
perete4=Entity(model="quad", texture="perete24.png", position=(12, -4), scale=(1, 7.5), collider="box")

def input(key):
    global viata, score
    if (key=='space up' or key=='left mouse down') and player.y>-4.2 and player.y<4.2 and viata==True:
        player.y+=1.2
        sunet.play()
    if key=='r up' and viata==False:
        viata=True
        lose.enabled=False
        player.y=0
        score=0
        perete1.x=8
        perete2.x=8
        perete3.x=14
        perete4.x=14
    if key=="q up":
        quit()
def update():
    global viata, score, score1
    if viata==True:
        score+=1
    score1.text=("Score:" + str(score))
    if player.y>-4.2 and player.y<4.2:
        player.y-=0.05
    if viata==True:
        perete1.x-=0.1
    if viata==True:
        perete2.x-=0.1
    if viata==True:
        perete3.x-=0.1
    if viata==True:
        perete4.x-=0.1


    if perete1.x<-5:
        perete1.x=8
    
    if perete2.x<-5:
        perete2.x=8

    if perete3.x<-5:
        perete3.x=8

    if perete4.x<-5:
        perete4.x=8


    if player.intersects(perete1):
        lose.enabled=True
        viata=False
    if player.intersects(perete2):
        lose.enabled=True
        viata=False
    if player.intersects(perete3):
        lose.enabled=True
        viata=False
    if player.intersects(perete4):
        lose.enabled=True
        viata=False


    if player.y<-4.2:
        lose.enabled=True
    
    if player.y>4.2:
        lose.enabled=True
    
app.run()