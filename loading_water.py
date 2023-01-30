from random import randint
from flet import *
c1 = "#87ceeb"
c2 = "#abddf1"
c3 = "#87ce4f"
c4 = "#73a3ff"


class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg
    self.water_running=True
    pg.horizontal_alignment = 'center'
    pg.vertical_alignment = 'center'
    self.init_helper()

  def init_helper(self):
    self.base()

  def move_water(self,e):
    while True:
      self.water.top -=1
      self.white_space.top -=1
      self.water.update()
      self.white_space.update()
      sleep(0.1)

  def animate_water(self,e):
    stopper = 0
    while self.water_running:
      if self.water_running == True:
        self.water.top -=1
        self.white_space.top -=1
        self.water.rotate +=.1
        self.white_space.rotate-=.1
        if stopper//3 <=100:
          self.percentage.value = str(stopper//3) + '%'
        self.percentage.update()
        self.water.update()
        self.white_space.update()
        sleep(0.1)
      stopper +=1
      if stopper >=310:self.water_running = False;break
 
  def base(self):
    self.percentage = Text(
            '0 %',
            color='green',
            size=50,
            right=100,
            top=100,

            
          )


    self.white_space = Container(
      data=False,
      animate_position=animation.Animation(500,AnimationCurve.DECELERATE),
      animate_rotation=animation.Animation(500,AnimationCurve.DECELERATE),
      rotate=0,
      top=-0,
      height=300,
      width=300,
      border_radius=135,
      bgcolor='#e3f0f5',
      clip_behavior=ClipBehavior.ANTI_ALIAS,
      
    )

    self.water = Container(
      animate_position=animation.Animation(500,AnimationCurve.DECELERATE),
      animate_rotation=animation.Animation(500,AnimationCurve.DECELERATE),
      data=False,
      top=-0,
      height=300,
      width=300,
      border_radius=120,
      bgcolor=c2,
      rotate=0.5,
      clip_behavior=ClipBehavior.ANTI_ALIAS,
    )

    self.c = Container(
    )


    self.pg.add(
      Stack(
        controls=[
          Container(
            height=300,
            width=300,
            border_radius=200,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            content=Stack(
              height=650,
              width=650,
              controls=[
                Container(
                  height=300,
                  width=300,
                  border_radius=200,
                  bgcolor=c1,
                  clip_behavior=ClipBehavior.ANTI_ALIAS,
                ),
                
                self.water,
                self.white_space,
              ]
            ),
          ),

          self.percentage,
        
        ]
      ),
        
        Row(
          spacing=30,
          alignment='center',
          controls=[
            Container(
              on_click=self.animate_water,
              alignment=alignment.center,
              
              height=50,width=50,bgcolor='green',margin=margin.only(top=200),border_radius=15,content=Text(
                'Start'
              )
            ),
            Container(
              alignment=alignment.center,
              on_click=self.move_water,
              height=50,width=50,bgcolor='red',margin=margin.only(top=200),border_radius=15,content=Text(
                'Stop'
              )
            )
          ]
        )
    )


app(target=App)    