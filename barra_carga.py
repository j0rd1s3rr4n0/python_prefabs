import time

def get_base_element(num):
    b_blassic = '▒'
    b_classic_two = '▢'
    b_volume = '▁'
    b_circle = ' '
    b_world_war = '卐'
    return ' '

def get_element_selector(element):
    r_classic = ['█']
    r_classic_two = ['■']
    r_volume = ['▁', '▂', '▃', '▅', '▆', '▇']
    r_circle = ['◐', '◑', '◒', '◓']
    r_world_war = ['☭']
    r_cross_dotted = ['⋮', '⋰', '⋯', '⋱']
    b_cross_dotted = ' '
    
    if element == 1:
        return r_classic
    elif element == 2:
        return r_classic_two
    elif element == 3:
        return r_volume
    elif element == 4:
        return r_circle
    elif element == 5:
        return r_world_war
    elif element == 6:
        return r_cross_dotted
    else:
        return r_classic

def anim_rigt(elements, type, BAR_LEN):
    frame = i % len(elements)
    base_element = str(get_base_element(type))
    print(f'\r[{elements[frame] * i:<{BAR_LEN}}{base_element}]', end='')

def anim_left(elements, type, BAR_LEN):
    frame = i % len(elements)
    base_element = str(get_base_element(type))
    print(f'\r[{elements[frame] * i:>{BAR_LEN}}{base_element}]', end='')

def anim_center(elements, type, BAR_LEN):
    frame = i % len(elements)
    base_element = str(get_base_element(type))
    print(f'\r[{elements[frame] * i:^{BAR_LEN}}{base_element}]', end='')


type = int(input("Tipo de carácter > "))   

BAR_LEN = int(input("Longitud de la barra > "))
elements = get_element_selector(type)

for i in range(BAR_LEN + 1):
    anim_rigt(elements=elements, type=type, BAR_LEN=BAR_LEN)
    time.sleep(0.1)

for i in range(BAR_LEN + 1):
    anim_left(elements=elements, type=type, BAR_LEN=BAR_LEN)
    time.sleep(0.1)

for i in range(BAR_LEN + 1):
    anim_center(elements=elements, type=type, BAR_LEN=BAR_LEN)
    time.sleep(0.1)
