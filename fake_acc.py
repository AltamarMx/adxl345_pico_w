import time, random

# Parámetros
noise          = 0.05        # ruido ±0.05 g
dt             = 0.1         # muestreo cada 0.1 s
stage_duration = 5           # duración de cada estado (s)

# Todas las combinaciones de -1,0,1 en 3 ejes, excepto (0,0,0)
opts = [-1.0, 0.0, 1.0]
states = [(x,y,z) for x in opts for y in opts for z in opts if (x,y,z) != (0.0,0.0,0.0)]

# Estado inicial: uno cualquiera distinto de cero
base = random.choice(states)
# Momento de la próxima transición
next_switch = time.time() + stage_duration

while True:
    now = time.time()

    # Cada stage_duration segundos, cambiamos de estado
    if now >= next_switch:
        # Elegimos un nuevo estado distinto del actual
        new_base = random.choice(states)
        while new_base == base:
            new_base = random.choice(states)
        base = new_base
        next_switch += stage_duration

    # Genera lectura con ruido uniforme ±noise
    x = base[0] + (random.random()*2*noise - noise)
    y = base[1] + (random.random()*2*noise - noise)
    z = base[2] + (random.random()*2*noise - noise)

    # Imprime valores como en un acelerómetro real (en g)
    print("{:+.3f},{:+.3f},{:+.3f}".format(x, y, z))

    time.sleep(dt)

