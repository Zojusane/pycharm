def guest_decide():
    guest_list = ['mark', 'peanut', 'langx', 'theshy', 'rookie', 'baolan', 'jackeylove']
    print(guest_list)
    print(f"{guest_list[1]} can't join the party because of the shit in his world champion game")
    guest_list[1] = 'knight'
    for value in guest_list:
        print(f"Hello, {value.title()}! You have been invited in the party. Sincerely hope you here!")
    guest_list.insert(0, 'ning')
    guest_list.append('uzi')
    while len(guest_list) > 3:
        guest_leave = guest_list.pop()
        if guest_leave != 'uzi':
            print(f"{guest_leave.title()},sorry! you're out")
        else:
            guest_list.insert(0, 'uzi')
            print(f"{guest_leave.title()},welcome!")
    print(guest_list)
    for value in guest_list:
        if value != 'uzi':
            print(f"{value.title()},welcome!")
    print(guest_list)
    del guest_list[0], guest_list[1]
    if len(guest_list) == 0:
        print("it's done")
    else:
        print(guest_list)
if __name__=='__main__':
    guest_decide()
