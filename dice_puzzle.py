import numpy as np
import matplotlib.pyplot as plt

def get_dice_prob_distribution(num_dice):
	assert(num_dice >= 1)
	prob_distribution = dict.fromkeys( (i for i in range(1, 6 * num_dice + 1)), 0)
	value_sums = [value for value in range(1, 7)]

	for die in range(1, num_dice):
		value_sums = [value_sum + new_value for new_value in range(1, 7) for value_sum in value_sums]

	for value_sum in value_sums:
		if not value_sum in prob_distribution:
			prob_distribution[value_sum] = 0
		prob_distribution[value_sum] += 1. / len(value_sums)

	return prob_distribution

def get_mapping_prob_distribution(mapping, num_dice):
	prob_distribution = dict.fromkeys((i for i in range(1, 6 * num_dice + 1)), 0)
	value_sums = [sum(map(int, duplet)) for triplet, duplet in mapping.iteritems()]

	for value_sum in value_sums:
		prob_distribution[value_sum] += 1. / len(value_sums)

	return prob_distribution

def create_mapping():
	three_dice_combos = [[i, j, k] for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]
	mapping = {}
	for triplet in three_dice_combos:
		pairs = []
		for i in range(0, len(triplet) - 1):
			pairs.append([triplet[i], triplet[i + 1]])
		# Sums of pairs mapped to new values
		# 2, 3, 4, 5, 6, 7, 8, 9,10,11,12
		# 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5
		duplet = [(sum(pair) - 2) % 6 + 1 for pair in pairs]
		mapping[''.join(str(t) for t in triplet)] = ''.join(str(d) for d in duplet)

	return mapping

if __name__ == '__main__':
	p_two_dice = get_dice_prob_distribution(num_dice = 2)
	mapping = create_mapping()
	probabilities = get_mapping_prob_distribution(mapping, num_dice = 2)
	print "Mapping distribution vs 2-dice probabilities:"
	print '\n'.join('Sum = {}: {} (expected : {})'.format(key, value, p_two_dice[key]) for key, value in probabilities.iteritems())

	draw_mapping(mapping)
	while(True):
		input_value = raw_input('Enter a triplet (eg. 632) or q to quit:')

		if input_value.lower() == "q":
			break

		triplet = str(input_value)

		if str(triplet) in mapping:
			print 'Equivalent 2-die roll: {}'.format(mapping[str(triplet)])
		else:
			print 'Something went wrong. No matching die-roll found for {}'.format(triplet)
