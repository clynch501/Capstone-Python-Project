#Part 3: Basketball Ticket Sales
# Total ticket revenue
def main():
    name = input('What is your name?')
    print('Welcome', name, 'to my basketball ticket revenue calculator!')
    box_tix = box()
    tier_1_tix = tier_1()
    tier_2_tix = tier_2()
    tier_3_tix = tier_3()
    total_revenue = box_tix*200 + tier_1_tix*50 + tier_2_tix*30 + tier_3_tix*10
    print('The number of box office tickets sold was', box_tix,'.')
    print('The number of tier 1 tickets sold was', tier_1_tix,'.')
    print('The number of tier 2 tickets sold was', tier_2_tix,'.')
    print('The number of tier 3 tickets sold was', tier_3_tix,'.')
    print('The total revenue for the basketball game was $',total_revenue,'.')
    
# Box tickets
def box():
    box_sold = int(input('How many box office tickets were sold?'))
    # Since there is a limited number of seats.
    # I have made an error message for when the input is greater than 50.
    while box_sold > 50:
        print('Error. Seats limited to 50. Please enter a value between 0 and 50.')
        box_sold = int(input('How many box office tickets were sold?'))
    return box_sold


# Tier 1 tickets
def tier_1():
    tier_1_sold = int(input('How many tier 1 tickets were sold?'))
    # There is a limit of 200 tier 1 seats.
    while tier_1_sold > 200:
        print('Error. Seats limited to 200. Please enter a value between 0 and 200.')
        tier_1_sold = int(input('How many box office tickets were sold?'))
    return tier_1_sold

# Tier 2 tickets
def tier_2():
    tier_2_sold = int(input('How many tier 2 tickets were sold?'))
    # There is a limit of 400 tier 2 seats.
    while tier_2_sold >400:
        print('Error. Seats limited to 400. Please enter a value between 0 and 400.')
        tier_2_sold = int(input('How many tier 2 tickets were sold?'))
    return tier_2_sold


# Tier 3 tickets
def tier_3():
    tier_3_sold = int(input('How many tier 3 tickets were sold?'))
    # There is a limit of 600 tier 3 seats.
    while tier_3_sold >600:
       print('Error. Seats limited to 600. Please enter a value between 0 and 600.')
       tier_3_sold = int(input('How many tier 3 tickets were sold?'))
    return tier_3_sold

main()

# Exit prompt
def goodbye():
    goodbye = input('Do you want to estimate the revenue for another event?')
    if goodbye == 'yes':
        main()
    else:
            print('Thank you for using my basketball ticket revenue program. Goodbye!')
goodbye()
