amtnums = input("How many numbers are you entering?")
totalnum = input("What is the total of the numbers?")
intamtnums = int(amtnums)
inttotalnum = int(totalnum)
file = open("Percentages.txt", "w")
for i in range(0, intamtnums):
	num = input("Enter number")
	percentage = float((1. * num/inttotalnum) * 100)
	roundedpercentage = round(percentage,2)
	file.write("Percentage of " + str(num) + " = " +str(roundedpercentage)+ "% \n")
file.write("Total: " + str(totalnum))	


