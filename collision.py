from flet import *



class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg
    self.init_helper()

  def init_helper(self):
    self.base()


  def base(self):
    self.pg.add(
      Container(
        expand=True,
        bgcolor='blue',
        content=Column(
          alignment='center',
          horizontal_alignment='center',
          controls=[
            Container(
              height=120,
              width=170,
              gradient=LinearGradient(
                colors=[]
              )
            ),
            Container(

            )
          ]

        )
      )
    )


app(target=App)    