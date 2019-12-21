# Read & print the first 3 lines
filename = 'moby_dick.txt'
with open(filename) as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
#Or 
# Open a file: file
#file = open("moby_dick.txt", mode = 'r')
# 'r' for reading mode
# Print it
#print(file.read())

# Check whether file is closed
#print(file.closed)

# Close file
#file.close()

# Check whether file is closed

#print(file.closed)