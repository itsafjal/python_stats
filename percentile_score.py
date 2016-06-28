#! /usr/bin/python


def Percentile_calculater(scores, your_score):
	cnt = 0
	for score in scores:
		if score<=your_score:
			cnt += 1
	
	result = (cnt*100)/len(scores)
	return result

scores= [11,22,33,44,55,66,77]
your_score = 55

myresult = Percentile_calculater(scores, your_score)

print myresult
