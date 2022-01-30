def Authenticated_National_Code(Code):
    rank = 10
    some = 0
    for i in Code:
        some += rank * int(i)
        if rank == 2:
            break
        rank -= 1
    left_over = some % 11

    if left_over >= 2:
        number_control = 11 - left_over
    else:
        number_control = left_over

    if number_control == int(Code[9]):
        return True
    else:
        return False
