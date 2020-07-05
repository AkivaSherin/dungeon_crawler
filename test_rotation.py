state["pixel_bullet_x"].append(
    state["pixel_guy_x"] + pixel_guy_width / 2 + 70 * math.cos(math.radians(state["pixel_guy_rotation"])))
state["pixel_bullet_y"].append(
    state["pixel_guy_y"] + pixel_guy_height / 2 + -70 * math.sin(math.radians(state["pixel_guy_rotation"])))