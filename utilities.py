import minimization as m


def collect_automaton(alphabets, final_states, states, automaton_list, case_number):
    aux_states = int(input())
    aux_alphabet = input().lower()
    alphabets.append(aux_alphabet.split(" "))
    bandera = False
    while not bandera:
        aux_final_states = input().split(" ")
        if m.check_final_states(aux_final_states, aux_states):
            bandera = True
    final_states.append([int(state) for state in aux_final_states])
    aux_matrix = []
    aux_states_list = []
    for row in range(aux_states):
        aux_row = input().split(" ")
        aux_matrix.append([int(state) for state in aux_row[1:]])
        aux_states_list.append(int(aux_row[0]))
    states.append(aux_states_list)
    automaton_list.append(aux_matrix)


def make_pairs(states, pairs_general):
    pairs = []
    for i in range(len(states)):
        for j in range(len(states)):
            pair = {i, j}
            if pair not in pairs and i != j:
                pairs.append(pair)
    pairs_general.append(pairs)


def deploy_equivalent(unmarked_pairs):
    string = ""
    for i in range(len(unmarked_pairs)):
        pair = unmarked_pairs[i]
        aux_list = list(pair)
        aux_list.sort()
        string += f"({aux_list[0]}, {aux_list[1]})"
        if i != len(unmarked_pairs) - 1:
            string += " "
        else:
            string += "\n"
    return string
