from flet import *


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

  def move_ball(self,e):
    pass


  def base(self):
    self.ball =Container(
        height=8,width=8,border_radius=8,bgcolor='black'
      )


    self.c = Container(
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
            content=Stack(
              controls=[
                Row(
                  height=50,
                  width=50,
                  alignment='center',
                  vertical_alignment='center',
                  controls=[
                    Container(
                    height=50,
                    width=50,
                    # bgcolor='white',
                    content=Row(
                      alignment='spaceBetween',
                      vertical_alignment='end',
                      controls=[
                        Container(
                          height=30,
                          width=8,
                          bgcolor='black'
                        ),
                        Container(
                          height=20,
                          width=8,
                          bgcolor='black'
                        ),
                        Container(
                          height=10,
                          width=8,
                          bgcolor='black'),
                        Container(
                          height=5,
                          width=8,
                          bgcolor='black'
                        ),
                      ]
                    )
                  )
                  ]
                ),
              
              self.ball,
              ]
            )
          ),
          Container(

          )
        ]

      )
    )


    self.pg.add(
      self.c,
      Container(
        on_click=self.move_ball,
        height=50,width=50,bgcolor='green',border_radius=12
      )
    )


app(target=App)    