def check_final_states(final_states, num_states):
    for i in range(len(final_states)):
        if int(final_states[i]) >= num_states:
            return False
    return True


def first_step(final_states, unmarked_pairs, marked_pairs):
    remove_later_pairs = []
    for pair in unmarked_pairs:
        aux_pair = list(pair)
        condition1 = aux_pair[0] in final_states and aux_pair[1] not in final_states
        condition2 = aux_pair[1] in final_states and aux_pair[0] not in final_states
        if condition1 or condition2:
            marked_pairs.append(pair)
            remove_later_pairs.append(pair)

    for pair in remove_later_pairs:
        unmarked_pairs.remove(pair)


def second_step(states, unmarked_pairs, marked_pairs, function, alphabet):
    remove_later_pairs = []
    for pair in unmarked_pairs:
        aux_pair = list(pair)
        for number in range(len(alphabet)):
            new_pair = {function[states.index(aux_pair[0])][number], function[states.index(aux_pair[1])][number]}
            if new_pair in marked_pairs and new_pair not in remove_later_pairs:
                marked_pairs.append(pair)
                remove_later_pairs.append(pair)
                break

    for pair in remove_later_pairs:
        unmarked_pairs.remove(pair)


def final_step(states, unmarked_pairs, marked_pairs, function, alphabet):
    bandera = True
    while bandera:
        aux_unmarked = unmarked_pairs[:]
        second_step(states, unmarked_pairs, marked_pairs, function, alphabet)
        if aux_unmarked != unmarked_pairs:
            aux_unmarked = unmarked_pairs[:]
        else:
            bandera = False
