data = """Add Data Here"""

data_list = data.split("\n")

x = 1
cycles = 0 
total = 0 
beam_pos = 0 
processing = False
line = 0 
for i in range(240):
    if beam_pos > 39:
        beam_pos = 0 
        print("")
    if beam_pos <= x+1 and beam_pos >= x-1:
        print("#", end = '')
    else:
        print(" ", end = '')
    if cycles == 20 or cycles == 60 or cycles == 100 or cycles == 140 or cycles == 180 or cycles == 220:
        total += (cycles*x)
    if processing == False:
        if data_list[line] == "noop":
            cycles += 1 
            beam_pos += 1
            line += 1
        elif data_list[line][:4] == "addx":
            processing = True
            cycles += 1 
            beam_pos += 1
    elif processing == True:
        cycles += 1
        beam_pos += 1
        x += int(data_list[line][4:])
        line += 1
        processing = False
    

print()   
print(cycles)
print(total)