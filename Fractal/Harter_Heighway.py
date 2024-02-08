import turtle

# screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(3 * WIDTH, 3 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings
dummy = turtle.Turtle()
dummy.pensize(3)
dummy.speed(0)
dummy.setpos(-WIDTH // 4, -HEIGHT // 4 - 25)
dummy.color('green')

# l-system settings
gens = 13
axiom = 'XY'
chr_1, rule_1 = 'X', 'X+YF+'
chr_2, rule_2 = 'Y', '-FX-Y'
step = 4
angle = 90


def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else 
                    rule_2 if chr == chr_2 else chr for chr in axiom]) 


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


for gen in range(gens):
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'generation: {gen}', align="left", font=("Arial", 60, "normal"))

    dummy.setheading(0)
    dummy.goto(-WIDTH // 6, HEIGHT // 6)
    dummy.clear()

    length = step / pow(3, gen)
    for chr in axiom:
        if chr == chr_1 or chr == chr_2:
            dummy.forward(step)
        elif chr == '+':
            dummy.right(angle)
        elif chr == '-':
            dummy.left(angle)

    axiom = apply_rules(axiom)

screen.exitonclick()