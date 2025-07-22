# The text you want to write
text = """Hello, world!
This is a simple example of writing text to a file.
You can write multiple lines like this."""

# Open a file in write mode ('w')
with open('example.txt', 'w') as file:
    file.write(text)

print("Text written to example.txt")