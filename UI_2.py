i = 0
i = int(i)
i_1 = 1
i_1 = int(i_1)
final = []

Unknown_Counter = 1
Unknown_Counter = int(Unknown_Counter)

counter = input("Inter Your Equales Number")
counter= int (counter)

while counter > i :
    x = input("inter your X" + str(Unknown_Counter) + "_" + str(i_1))
    final.append(x)


    i= i+1

    i_1 = i_1+1
    if len(final) == counter or len(final)%counter == 0:
        i = 0
        i = int(i)
        i_1 = 1
        i_1 = int(i_1)
        Unknown_Counter = Unknown_Counter+1
        Unknown_Counter = int(Unknown_Counter)
    if Unknown_Counter > counter:
        break