# __copy__ right:: Joseph Rice
# Vpython Pong
## code
print("You may use this code but do not clam it as yours\n happy codeing")
print("zoom in and out for a better view for the Board"\
,"\nHold the right and left of the mouse")
from time import sleep
from visual import *
scene.width,scene.height = 1000,1000

scene.title = "Pong!"
court = box(pos=(0,0,-5),size=(5,10,0),color=color.white)
Gamelabel = label(pos=(0,6,-5),text = "Right Arrow move right; Left Arrow move left",color = color.red)
Gamelabel = label(pos=(0,7,-5),text = "'a' move Left; 'd' move Right",color = color.blue)

class Pong:

    def __init__(self,x,y,z,width,length,deepth,color):
        """ x pos, ypos, zpos,deepth,color """
        ## going to make methods for corner Uper Right, Uper Left, Down Right, Down left # *** IMPORTANT FOR COLISION ON THE WALLS
        self.x,self.y,self.z,self.length,self.width,self.deepth,self.color =\
         x,y,z,length,width,deepth,color
        self.pong,self.pong.velocity= box(pos=(self.x,self.y,self.z),size=\
        (self.width,self.length,self.deepth),color=self.color),vector(1,0,0)
        # get program to incriment this to move object
    # I might have to change this this is the fixed value we might have to change it because it will be moveing
    def get_X(self):
        return self.pong.pos.x
    def get_Y(self):
        return self.pong.pos.y
    def Upper_rightx(self):
        """ current Position of upper right x corner"""
        """ URX stands for UPPER RIGHT X... ect """
        URX = self.pong.pos.x + self.width/2
        return URX
    def Upper_righty(self):
        """current Pos of right y"""
        URY = self.pong.pos.y + self.length/2
        return URY
    def Lower_rightx(self):
        """ lower right courner """
        LRX = self.pong.pos.x + self.width/2
        return LRX
    def Lower_righty(self):
        """ lower right courner """
        LRY = self.pong.pos.y - self.length/2
        return LRY
    def Upper_leftx(self):
        """ upper left courner """
        ULX = self.pong.pos.x - self.width/2
        return ULX
    def Upper_lefty(self):
        """ upper left courner """
        ULY = self.pong.pos.y + self.length/2
        return ULY
    def Lower_leftx(self):
        """ lower left corner """
        LLX = self.pong.pos.x - self.width/2
        return LLX
    def Lower_lefty(self):
        """ Lower left corner """
        LLY = self.pong.pos.y - self.length/2
        return LLY
    def update_pos(self,direction,speed=0.001):
        """ nagative and positive numbers for different pos on x axis nagative for right and positve for left"""
        ## movement for the right and left no up and down
        """ ZERO IF YOU DO NOT WANT IT TO MOVE ALL """
        if self.pong.pos.x <= 5/2 and self.pong.pos.x >=-5/2:
            self.pong.velocity = vector(direction*1*5,0,0)
            self.pong.pos.x += self.pong.velocity.x*speed
        elif self.pong.pos.x  >=5/2:
            self.pong.velocity = vector(-1*10,0,0)
            self.pong.pos.x += self.pong.velocity.x*speed
        elif self.pong.pos.x <=-5/2:
            self.pong.velocity = vector(10,0,0)
            self.pong.pos.x += self.pong.velocity.x*speed
    def update(self,speed):
        """ this updates the NONE PLAYER PONG"""

        if self.pong.pos.x + self.width/2 >= 5/2 or self.pong.pos.x - self.width/2 <= -5/2:
            self.pong.velocity.x = -self.pong.velocity.x
        self.pong.pos.x += self.pong.velocity.x * speed

class ball:
    def __init__(self,x,y,z,radius,color,vector):
        """" x pos, y pos, z pos, radius, color , vector from list"""
        # set z to -5 if you want it on board
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.length = 2 * self.radius
        self.color = color
        self.ball = sphere(pos=(self.x,self.y,self.z),radius=self.radius,color=self.color)
        self.ball.velocity = vector
    def ball_update(self,deltat,ball_crash=0):
        # enter a small number like 0.02
        """ This will serve as an update for the position use a while loop"""
        speed_radius = deltat/self.radius ## I want the size to affect the speed
        if self.ball.pos.x >= 5/2 or self.ball.pos.x <= -5/2:
            self.ball.velocity.x = -self.ball.velocity.x
        if self.ball.pos.y >= 5 or self.ball.pos.y <-5:
            self.ball.velocity.y  = -self.ball.velocity.y
        if ball_crash != 0:
            # this is so the balls dont pass through each other
            self.ball.velocity.y= -self.ball.velocity.y

        self.ball.pos = self.ball.pos + self.ball.velocity * speed_radius
    def radius(self):
        return self.radius
    def getPos_x(self):
        """ this gets the current value of x so that the computer can regester that the ball has hit the pong board"""
        return self.ball.pos.x
    def getPos_y(self):
        """ this gets the current value of y so that the computer can regester that ball has hit the pong board"""
        return self.ball.pos.y
    def Set_back(self):
        ## sets back ball to starting position
        self.ball.pos.x,self.ball.pos.y,self.ball.z = self.x,self.y,self.z

def pong_and_crash(pong,ball):
    """ short cut for the ball and pong colide"""
    if float(pong.Upper_rightx()) >= float(ball.getPos_x()) and  float(ball.getPos_x())\
     >= float(pong.Upper_leftx()) \
       and float(pong.Upper_lefty()) >= float(ball.getPos_y()) and float(ball.getPos_y())\
        >=float(pong.Lower_lefty()):
        ball.ball_update(0.001,1)
        n = 1
    else:
        n = 0
    return n

value =[vector(-7,-5,0),vector(0.5,3,0),vector(0.5,-3,0),vector(7,-10,0),vector(10,-10,0)]
white,black,orange,yellow,green,red,blue,magenta\
=color.white,color.black,color.orange,color.yellow,color.green,color.red,color.blue\
,color.magenta

net1 = Pong(0,4.9,-5,3,0.2,0,red)
net2 = Pong(0,-4.9,-5,3,0.2,0,blue)
player_1 = Pong(0,3,-5,1,0.2,0,red)
player_2 = Pong(0,-3,-5,1,0.2,0,blue)
Ball = ball(0,0,-5,0.1,magenta,value[1])

score_label = label(pos=(6,0,-5),text=("Score ball into Goal To win"),color=color.orange)
score_board = label(pos=(-8,0,-5),text = ("\n" + "PRESS 's' 3 TIMES to start or 'q' to add a ball"))
score_red = label(pos=(0,4,-5),text = ("  "))
score_blue = label(pos=(0,-4,-5),text=("  "))
def main():
    while True:
        print("____Hit {Enter}____" + "\n enter speed of the ball below")
        speed = 10

        if scene.kb.getkey() == "q":
            break
            quit()
    ##    speed = eval(input(" Enter speed of ball "))
        if scene.kb.getkey() == "s":
            start = scene.kb.getkey()

            sleep(1)
            if start == "s":
                score_board.text = "Game On"
                score = 0
                score1 = 0

                n = speed*10**-4
                while True:
                    rate(90)
                    Ball.ball_update(n)

                    if scene.kb.keys:
                        movement = scene.kb.getkey()
                        if movement == 'right':
                            player_1.update_pos(1,0.1)
                        if movement == "left":
                            player_1.update_pos(-1,0.1)
                        if movement == 'd':
                            player_2.update_pos(1,0.1)
                        if movement =="a":
                            player_2.update_pos(-1,0.1)

                    if pong_and_crash(net1,Ball):
                        score_board.text = 'Blue Wins!'
                        score_label.text  = "Press 's'"

                        break
                    if pong_and_crash(net2,Ball):
                        score_board.text = 'Red Wins!'
                        score_label.text = "Press 's'"
                        break

                    if pong_and_crash(player_1,Ball):
                        n += n/4
                        pong_and_crash(player_1,Ball)
                        pong_and_crash(player_1,Ball)
                        score +=1
                        score_red.text = str(score)

                    if pong_and_crash(player_2,Ball):
                        n += n/4
                        pong_and_crash(player_2,Ball)
                        pong_and_crash(player_2,Ball)
                        score1 +=1
                        score_blue.text = str(score1)
                Ball.Set_back()

for i in range(10):
    main()









