print("Welcome to 2-player Battleships!")
print("Please enter your name.")
name1 = input("Player 1's name: ")
name2 = input("Player 2's name: ")
table = [[0,0,0,0,0,[0]],[0,0,0,0,0,[1]],[0,0,0,0,0,[2]],[0,0,0,0,0,[3]],[0,0,0,0,0,[4]]]
for ya in table:
    print(ya)
print([0,1,2,3,4])

print("{}, please enter the coordinates for your ship.".format(name1))
a = int(input("X(0/1/2/3/4): "))
b = int(input("Y(0/1/2/3/4): "))

i = 0
while (i < 20):
    print(print("-----------line--to--ignore------------"))
    i += 1

for ya in table:
    print(ya)
print([0,1,2,3,4])
print("{}, please enter the coordinates for your ship.".format(name2))
c = int(input("X(0/1/2/3/4): "))
d = int(input("Y(0/1/2/3/4): "))

j = 0
while (j < 20):
    print(print("-----------line--to--ignore------------"))
    j += 1

print("Game is starting...")

while True:
    print("It is {}'s turn.".format(name1))
    print("Enter the coordinates to fire upon.")

    x1 = int(input("X: "))
    y1 = int(input("Y: "))
    table[x1][y1] = 1
    for ya in table:
        print(ya)
    print([0,1,2,3,4])

    if x1 != c or y1 != d:
        print("Miss...switching players!")
        print("It is {}'s turn.".format(name2))
        print("Enter the coordinates to fire upon.")

        x2 = int(input("X: "))
        y2 = int(input("Y: "))
        table[x2][y2] = 2
        for ya in table:
            print(ya)
        print([0,1,2,3,4])
        if x2 != a or y2 != b:
            print("Miss...switching players!")

        else:
            print("{} wins!!.".format(name2))
            print("Hit!You have sunk {}'s ship!".format(name1))

    else:
        print("{} wins!!.".format(name1))
        print("Hit!You have sunk {}'s ship!".format(name2))

    if x1 == c and y1 == d or x2 == a and y2 == b:
        print("Game over")
        break
