#from prime import Prime
#from utils import ListUtil

def get_answer():
   
    sum = 0
    for value in range(1,1001):
        sum += value ** value
    return str(sum)[-10:]


if __name__ == "__main__":
	print("Answer: {0}".format(get_answer()))
