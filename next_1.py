from flet import *
c1 = "#6225e6"
c2 = "#fbc638"
w = 250
w2 = 300
h = 80
# br =0
br =w//4
d = 6
d2 = 2
def main(page: Page):
  page.vertical_alignment = 'center'
  page.horizontal_alignment = 'center'

  def do_something():
    n = 0
    while True:
      print(n)
      n+=1

  def c1_hover(e: HoverEvent):
    if e.data == 'true':
      _c1.width = w2
      _c2.width = w2
      _c2.bottom = d2
      _c2.right = d2
      _c2.bgcolor= c2
      next_text.margin = margin.only(right=20)
      a1.offset = transform.Offset(-0.5,0)
      a3.offset = transform.Offset(0.5,0)
    else:
      next_text.margin = 0
      a1.offset = transform.Offset(0,0)
      a3.offset = transform.Offset(0,0)
      _c2.bgcolor= 'black'
      # _c2.opacity = 100
      _c2.bottom = d
      _c2.right = d
      _c1.width = w
      _c2.width = w
    next_text.update()
    a1.update()
    _c1.update()
    _c2.update()

  next_text = Container(
    animate=animation.Animation(500,'decelerate'),
    margin=0,
    content=Text(
      'NEXT',
      size=40,
      weight=FontWeight.W_900,
      italic=True
    )
  )
  a1 = Container(
    animate_offset=animation.Animation(500,'decelerate'),
    offset=transform.Offset(0,0),
    content=Icon(
      icons.ARROW_FORWARD_IOS,
      size=35,

    ),
  )


  a2= Container(
    animate_offset=animation.Animation(500,'decelerate'),
    offset=transform.Offset(0,0),
    content=Icon(
      icons.ARROW_FORWARD_IOS,
      size=35,

    ),
  )


  a3 = Container(
    animate_offset=animation.Animation(500,'decelerate'),
    offset=transform.Offset(0,0),
    content=Icon(
      icons.ARROW_FORWARD_IOS,
      size=35,

    ),
  )


  _c1 = Container(
    animate=animation.Animation(500,'decelerate'),
    on_hover=c1_hover,
    padding=padding.only(left=50,right=20),
    alignment=alignment.center,
    height=h,
    width=w,
    bgcolor=c1,
    margin=10,
    border_radius = BorderRadius(topLeft=br, topRight=0, bottomLeft=0, bottomRight=br),
    content=Row(
      vertical_alignment='center',
      controls=[
        next_text,
        Stack(
          controls=[
            a1,a2,a3
          ]
        )
      ]
    )
  )
  
  _c2 = Container(
    animate_position=animation.Animation(500,'decelerate'),
    animate_opacity=animation.Animation(500,'decelerate'),
    animate=animation.Animation(500,'decelerate'),
    bottom=d,
    right=d,
    height=h,
    width=w,
    bgcolor='black',
    border_radius = BorderRadius(topLeft=br, topRight=0, bottomLeft=0, bottomRight=br)
  )


  page.add(
    Container(
      height=500,
      width=500,
      bgcolor='white24',
      content=Column(
        alignment='center',
        horizontal_alignment='center',
        controls=[
          Stack(
            controls=[
              _c2,
              _c1,
            ]
          ),
        ]
      )
    )
  )

app(target=main)