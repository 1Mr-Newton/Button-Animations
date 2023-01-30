from random import randint
from flet import *
c1 = "#1bb3fd"
c2 = "#216bff"
c3 = "#6bcaff"
c4 = "#73a3ff"


class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg
    self.init_helper()

  def init_helper(self):
    self.base()

  def move_c(self,e: HoverEvent):
    # if e.data == 'true':
      for i in range(20):
        self.c.offset = transform.Offset((randint(1,2)/10),(randint(1,2)/10))
        sleep(0.1)
        self.c.update()


    #   self.c.offset = transform.Offset(0.2,0.1) 
    # else:
    #   self.c.offset = transform.Offset(0,0) 
    # self.c.update()


  def base(self):
    self.c = Container(
      on_click=self.move_c,
      offset= transform.Offset(0.0,0),
      animate_offset=animation.Animation(500,AnimationCurve.EASE_IN_CUBIC),
      expand=True,
      # bgcolor='blue',
      content=Column(
        alignment='center',
        horizontal_alignment='center',
        controls=[
          Container(
            padding=8,
            clip_behavior=ClipBehavior.ANTI_ALIAS,
            border_radius=12,
            height=120,
            width=170,
            gradient=LinearGradient(
              colors=[
                c1,
                c2
              ]
            ),
            content=Container(
              border_radius=12,
              # expand=True,
              width=160,
              height=110,
              gradient=LinearGradient(
                colors=[c3,c4]
              )
            )
          ),
          Container(

          )
        ]

      )
    )


    self.pg.add(
      self.c
    )


app(target=App)    