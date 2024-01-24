#define a function for counting emma
def count_emma(statement):
#for loop
    for i in range(len(statement) - 1):
#check if the substring of length 4 starting at the current index is equal to Emma
        if statement[i: i + 4] == 'Emma':
            count += 1
#if loop is finished return count 
    return count
#check the function and print the given statement