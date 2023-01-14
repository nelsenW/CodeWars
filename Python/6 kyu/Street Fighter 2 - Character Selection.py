def street_fighter_selection(fighters, i_pos, moves):
    ans = []
    pos = [i_pos[0], i_pos[1]]
    for move in moves:
        print(pos, move)
        if move == 'up':
            if pos[0] == 1:
                pos[0] -= 1
        elif move == 'down':
            if pos[0] == 0:
                pos[0] += 1
        elif move == 'right':
            pos[1] += 1
            pos[1] %= 6
        else:
            pos[1] -= 1
            pos[1] %= 6
        ans.append( fighters[pos[0]][pos[1]] )
    return ans