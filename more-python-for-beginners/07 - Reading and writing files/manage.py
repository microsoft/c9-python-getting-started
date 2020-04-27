# Open manage.txt file to write text
stream = open('manage.txt', 'wt')

#Write the word demo to the file stream
stream.write('demo!')

# Move back to the start of the file stream
stream.seek(0)

#write the word cool to the file stream
stream.write('cool')

#Flush the file stream contents to the file buffer
stream.flush()

# Flush the file stream and close the file
stream.close()
