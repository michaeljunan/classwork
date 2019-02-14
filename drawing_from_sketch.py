import arcade


WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 640, 100, 0, arcade.color.GO_GREEN)

arcade.draw_triangle_filled(200, 200, 160, 125, 240, 125, arcade.color.GREEN)

arcade.draw_xywh_rectangle_filled(190, 50, 20, 75, arcade.color.BROWN)

arcade.draw_triangle_filled(515, 200, 475, 125, 555, 125, arcade.color.GREEN)

arcade.draw_xywh_rectangle_filled(505, 50, 20, 75, arcade.color.BROWN)

arcade.draw_xywh_rectangle_filled(430, 50, 20, 75, arcade.color.BROWN)

arcade.draw_triangle_filled(440, 200, 400, 125, 480, 125, arcade.color.GREEN)








arcade.draw_circle_filled(540, 380, 50, arcade.color.RED_ORANGE)

# End drawing
arcade.finish_render()
arcade.run()