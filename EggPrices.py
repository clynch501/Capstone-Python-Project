#Part 1 Cheapest Eggs
name = input ('What is your name?:')
print ('Hello',name)
DozenEggs = (5.69/12)
EighteenEggs = (7.49/18)
TwentyfourEggs = (9.99/24)
Eggs = [DozenEggs, EighteenEggs, TwentyfourEggs]
Cheapest_Eggs = min(Eggs)
print ('The cheapest eggs are', f"{Cheapest_Eggs:.2f}", 'per egg which is the 18 eggs for $7.49')





