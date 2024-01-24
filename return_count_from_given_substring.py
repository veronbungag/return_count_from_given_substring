#define a function for counting emma
def count_emma(statement):
    #initialize count to 0
    count = 0
#for loop
    for i in range(len(statement) - 1):
#check if the substring of length 4 starting at the current index is equal to Emma
        if statement[i: i + 4] == 'Emma':
            count += 1
#if loop is finished return count 
    return count
#check the function and print the given statement
count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared", count, "times")