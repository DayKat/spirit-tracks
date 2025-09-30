
switch_sensitive_entrances = {
    "ToI B1 Ascent": 0b10
}

switch_logic = [
    # [entrance, exit, normal, *hard, *glitched]
    ["ToI Exit", "ToI 1f Switch Staircase", 0b10, 0b11],
    ["ToI Exit", "ToI 1f Descent", 0b11],
    ["ToI Exit", "ToI 1f Ascent", 0b11],
    ["ToI 1f Ascent", "ToI Exit", 0b11],
    ["ToI 1f Ascent", "ToI 1f Switch Staircase", 0b10, 0b11],
]

ruins_water = [

]