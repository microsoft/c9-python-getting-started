# Open output.txt as a text file for writing
stream = open('output.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H') # Write a single string 
stream.writelines(['ello',' ','world']) # Write one or more strings
stream.write('\n') # Write a new line

names = ['Susan','Christopher']
stream.writelines(names)

# Here's a neat trick to insert a new line between items in the list
stream.write('\n')  # Write a new line
stream.writelines('\n'.join(names)) 
stream.close() #Flush stream and close
