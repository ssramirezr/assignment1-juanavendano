import minimization as m
import utilities as u

alphabets = []
final_states = []
states = []
automatons = int(input())
automaton_list = []
unmarked_pairs = []
marked_pairs = []
output = []
string = ""
for case_number in range(automatons):
    u.collect_automaton(alphabets, final_states, states, automaton_list, case_number)
    u.make_pairs(states[case_number], unmarked_pairs)
    marked_pairs.append([])
    m.first_step(final_states[case_number], unmarked_pairs[case_number], marked_pairs[case_number])
    m.final_step(states[case_number], unmarked_pairs[case_number], marked_pairs[case_number], automaton_list[case_number], alphabets[case_number])
    output.append(unmarked_pairs[case_number])
    output[-1] = sorted(output[-1])
    string += u.deploy_equivalent(output[-1])
print(string.strip())