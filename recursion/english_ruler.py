# This is an English ruler
# Major Tick Length = 3
# Inches = 2
#
# --- 0
# -
# --
# -
# --- 1
# -
# --
# -
# --- 2


def draw_line(tick_length, tick_label=''):
    tick_symbol = '-'
    line = tick_symbol * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(central_tick_length):
    if central_tick_length > 0:
        draw_interval(central_tick_length - 1)
        draw_line(central_tick_length)
        draw_interval(central_tick_length - 1)


def draw_ruler(major_tick_length, inches):
    if inches > 0:
        draw_line(major_tick_length, '0')
        for i in range(1, inches + 1):
            draw_interval(major_tick_length - 1)
            draw_line(major_tick_length, str(i))


print(f"Ruler:: major_tick_length = 3, inches = 3\n\n")
draw_ruler(3, 3)
print('\n\n')


print(f"Ruler:: major_tick_length = 5, inches = 3\n\n")
draw_ruler(5, 3)
print('\n\n')