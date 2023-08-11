def average(array):
    return sum(array)/len(array)
numbers = input("Enter a list of numbers you want to find the average. Each number should be separated by a comma. ")
my_list = numbers.split(",")
final_list = [float(x) for x in my_list]
print("The average of the numbers you entered is ", average(final_list))