from project.datasets import Simple, Split, Xor

def classify_Simple(pt):
	if pt[0] < 0.5:
		return 1
	else: 
		return 0

def classify_Split(pt):
	if pt[0] < 0.2 or pt[0] > 0.8:
		return 1
	else: 
		return 0


N = 100
#Simple(N, vis=True).graph("initial", model=classify_Simple)
Split(N, vis=True).graph("initial", model=classify_Split)
