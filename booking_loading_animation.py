from flet import *



class App(UserControl):
  def __init__(self,pg:Page):
    super().__init__()
    self.pg = pg