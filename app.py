from flet import *
bgc = "#282828"
c1 = "#3d0b0b"
c2 = "#2b0808"
def main(pg: Page):
  pg.add(
    Container(
      # bgcolor='',
      expand=True,
      content=Column(
        alignment='center',
        horizontal_alignment='center',
        controls=[
          # Container(
          #   width=200,
          #   height=60,
          #   gradient=LinearGradient(
          #     colors=[
          #       c2,c1
          #     ],
          #     tile_mode=GradientTileMode.CLAMP,
          #     stops=[0.5,0.1,],
          #     rotation=1
              
          #   ),
          #   border=border.only(top=border.BorderSide(width=2,color='red',))
          # ),
          Container(
            width=200,
            height=70,
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
                Container(
                  gradient=SweepGradient(
                    colors=[
                      "red",
                      "#003d0b0b"
                    ],
                    stops=[0.2,0.4],
                    rotation=6
                    # start_angle=1,
                    # end_angle=3
                  ),
                  width=200,
                  height=70,
                  content=Row(
                    alignment='center',
                    vertical_alignment='center',
                    controls=[
                      Container(
                        width=193,
                        height=63,
                        gradient=LinearGradient(
                          colors=[
                            c2,c1
                          ],
                          tile_mode=GradientTileMode.CLAMP,
                          stops=[0.5,0.1,],
                          rotation=1
                        ),

                      )
                    ]
                  )
                )
              ]
            )
          ),
          Container(),
        ]
      )

    )
  )

app(target=main)