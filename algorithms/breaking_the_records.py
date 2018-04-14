def breakingRecords(scores):
	"""
	"""

	max_score = scores[0]
	min_score = scores[0]
	min_break = 0
	max_break = 0
	for score in scores[1:]:
		if score > max_score:
			max_score = score
			max_break += 1
		elif score < min_score:
			min_score = score
			min_break += 1

	return max_break, min_break


if __name__ == '__main__':
	breakingRecords()