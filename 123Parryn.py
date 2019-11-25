#   a123_apple_1.py
import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
screen_width = 400
screen_height = 400
letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U", "V", "W", "X", "Y", "Z"]

active_letters = []
apple_list = []
number_of_apples = 5

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

wn.bgpic("background.gif")
# apple = trtl.Turtle()
# apple.penup()
current_letter = "A"
wn.tracer(False)

def reset_apple(active_apple):
  global current_letter
  length_of_list = len(letter_list)
  if (length_of_list != 0):
    index = rand.randint(0,length_of_list)
    active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height)/2, (screen_height)/2))
    current_letter = letter_list.pop(index)
    draw_apple(active_apple, current_letter) 
    active_letters.append(current_letter)

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
  draw_letter(active_apple, letter)
  wn.update()

def drop_apple(letter):
  wn.tracer(True)
  index = active_letters.index(letter)
  active_letters.pop(index)

  active_apple = apple_list.pop(index)

  active_apple.goto(active_apple.xcor(), ground_height)
  active_apple.clear()
  active_apple.hideturtle()
  wn.tracer(False)
  reset_apple(active_apple)
  apple_list.append(active_apple)

def draw_letter(active_apple, letter):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

for i in range(number_of_apples):
    active_apple = trtl.Turtle(shape = apple_image)
    active_apple.penup()
    reset_apple(active_apple)
    apple_list.append(active_apple)





# draw_apple(apple, current_letter)

def check_apple_a():
  if ("A" in active_letters):
    drop_apple("A")

def check_apple_b():
  if ("B" in active_letters):
    drop_apple("B")

def check_apple_c():
  if ("C" in active_letters):
    drop_apple("C")

def check_apple_d():
  if ("D" in active_letters):
    drop_apple("D")

def check_apple_e():
  if ("E" in active_letters):
    drop_apple("E")

def check_apple_f():
  if ("F" in active_letters):
    drop_apple("F")

def check_apple_g():
  if ("G" in active_letters):
    drop_apple("G")

def check_apple_h():
  if ("H" in active_letters):
    drop_apple("H")

def check_apple_i():
  if ("I" in active_letters):
    drop_apple("I")

def check_apple_j():
  if ("J" in active_letters):
    drop_apple("J")

def check_apple_k():
  if ("K" in active_letters):
    drop_apple("K")

def check_apple_l():
  if ("L" in active_letters):
    drop_apple("L")

def check_apple_m():
  if ("M" in active_letters):
    drop_apple("M")

def check_apple_n():
  if ("N" in active_letters):
    drop_apple("N")

def check_apple_o():
  if ("O" in active_letters):
    drop_apple("O")

def check_apple_p():
  if ("P" in active_letters):
    drop_apple("P")

def check_apple_q():
  if ("Q" in active_letters):
    drop_apple("Q")

def check_apple_r():
  if ("R" in active_letters):
    drop_apple("R")

def check_apple_s():
  if ("S" in active_letters):
    drop_apple("S")

def check_apple_t():
  if ("T" in active_letters):
    drop_apple("T")

def check_apple_u():
  if ("U" in active_letters):
    drop_apple("U")

def check_apple_v():
  if ("V" in active_letters):
    drop_apple("V")

def check_apple_w():
  if ("W" in active_letters):
    drop_apple("W")

def check_apple_x():
  if ("X" in active_letters):
    drop_apple("X")

def check_apple_y():
  if ("Y" in active_letters):
    drop_apple("Y")

def check_apple_z():
  if ("Z" in active_letters):
    drop_apple("Z")
    

wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")

wn.listen()
trtl.mainloop()

