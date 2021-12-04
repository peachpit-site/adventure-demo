class Location:
    def __init__(self, short_description, long_description, n, s, e, w):
        self.short_description = short_description
        self.long_description = long_description
        self.n = n
        self.s = s
        self.e = e
        self.w = w

def find_location(name):
    for L in locations:
        if L.short_description == name:
            return L

file1 = open('dungeon.txt', 'r')
lines = file1.readlines()
locations = []

i = 0
while i < len(lines):
    short_description = lines[i]
    i = i + 2
    n = ''
    s = ''
    e = ''
    w = ''
    long_description = ''
    while lines[i] != '---\n':
        long_description = long_description + lines[i]
        i = i + 1
    i = i + 1
    while lines[i] != '---\n':
        if lines[i][:3] == 'n: ':
            n = lines[i][3:]
        if lines[i][:3] == 's: ':
            s = lines[i][3:]
        if lines[i][:3] == 'e: ':
            e = lines[i][3:]
        if lines[i][:3] == 'w: ':
            w = lines[i][3:]
        i = i + 1
    i = i + 2
    new_location = Location(short_description, long_description, n, s, e, w)
    locations.append(new_location)

player_location = locations[0]

# Now we REPL.

while True:
    print()
    print(player_location.short_description)
    print(player_location.long_description)
    new_location_name = ''
    while new_location_name == '':
        command = input('Your orders? ').rstrip()
        while not command in ['n','s','e','w']:
            print('I\'m sorry, I only understand the commands n, s, e, and w.')
            command = input().rstrip()
        if command == 'n':
            new_location_name = player_location.n
        if command == 's':
            new_location_name = player_location.s
        if command == 'e':
            new_location_name = player_location.e
        if command == 'w':
            new_location_name = player_location.w
        if new_location_name == '':
            print('You can\'t go in that direction.')
    player_location = find_location(new_location_name)   
