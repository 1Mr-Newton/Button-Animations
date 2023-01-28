from flet import *
import asyncio
bgc = "#282828"
c1 = "#3d0b0b"
c2 = "#2b0808"
red = '#d72525'

def main(pg: Page):
  
  # pg.bgcolor = colors.TRANSPARENT
  # pg.window_bgcolor = colors.TRANSPARENT
  # pg.window_title_bar_hidden =True
  # pg.window_frameless = False
  def animate_border(e):
    while True:
      c.gradient.rotation -= .1
      c.update()
      sleep(0.1)

        
      
  c  =  Container(
    on_hover=animate_border,
    gradient=SweepGradient(
      colors=[
        red,
        "#003d0b0b"
      ],
      stops=[0.2,0.4],
      rotation=6,
      tile_mode=GradientTileMode.REPEATED
    ),
    width=300,
    height=120,
    content=Row(
      alignment='center',
      vertical_alignment='center',
      controls=[
        Container(
          alignment=alignment.center,
          width=295,
          height=115,
          gradient=LinearGradient(
            colors=[
              c2,c1
            ],
            tile_mode=GradientTileMode.CLAMP,
            stops=[0.5,0.1,],
            rotation=1
          ),
          content=Text(
            'BUTTON',
            size=25,
            color='#f7d4d4'
          )
        )
      ]
    )
  )
              

  
  pg.add(
    Container(
      # bgcolor='',
      expand=True,
      content=Column(
        alignment='center',
        horizontal_alignment='center',
        controls=[
          
          Container(
            width=300,
            height=120,
            gradient=LinearGradient(
              colors=[
                c2,c1
              ],
              tile_mode=GradientTileMode.CLAMP,
              stops=[0.5,0.1,],
              rotation=1
              
            ),
            content=Row(
              alignment='center',
              vertical_alignment='center',
              controls=[
               c
              ]
            )
          ),
          
          Container(

          ),
        ]
      )

    )
  )

app(target=main)


# https://emojipedia.org/face-with-tears-of-joy/