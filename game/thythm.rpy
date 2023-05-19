screen rhythm_game():
     default rhythm_game_display = Rhythm()
     add Solid('#000')
     add rhythm_game_display

init python:
     class Rhythm(renpy.Displayable):
          def __init__(self):
               super(Rhythm, self).__init__()

               self.x_offset = 400
               self.track_bar_height = int(config.screen_height * 0.85)
               self.track_bar_width = 12
               self.horizontal_bar_height = 8

               # number of track bars
               self.num_track_bars = 4
               # drawing position
               self.track_bar_spacing = (config.screen_width - self.x_offset * 2) / (self.num_track_bars - 1)
               # the xoffset of each track bar
               self.track_xoffsets = {
               track_idx: self.x_offset + track_idx * self.track_bar_spacing
                    for track_idx in range(self.num_track_bars)
               }

               # define the drawables
               self.track_bar_drawable = Solid('#fff', xsize=self.track_bar_width, ysize=self.track_bar_height)
               self.horizontal_bar_drawable = Solid('#fff', xsize=config.screen_width, ysize=self.horizontal_bar_height)

               # record all the drawables for self.visit
               self.drawables = [self.track_bar_drawable,self.horizontal_bar_drawable]

          def render(self, width, height, st, at):
               render = renpy.Render(width,height)

               # draw the vertical tracks
               for track_idx in range(self.num_track_bars):
                    # look up the offset for drawing
                    x_offset = self.track_xoffsets[track_idx]
                    # y = 0 starts from the top
                    render.place(self.track_bar_drawable, x=x_offset, y=0)

               # draw the horizontal bar to indicate where the track ends
               # x = 0 starts from the left
               render.place(self.horizontal_bar_drawable, x=0, y=self.track_bar_height)
               return render

          def event(self, ev, x, y, st):
               print(f'hello {x} {y}')

          def visit(self):
               return self.drawables