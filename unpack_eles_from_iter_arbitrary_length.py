"""
You need to unpack N elements from an iterable, but the iterable
may be longer than N elements, causing a
"too many values to unpack" exception
"""
arr = [1, 2, 3, 4]
# Use star expressions.
a, b, *c = arr

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

name, email, *phone_number = record
print(name)
print(email)
print(phone_number)


"""
Extended iterable unpacking is tailor-made for unpacking iterables
of unkonwn or arbitrary length.

Often, these iteratbles have some known component or pattern in
their construction ("Everything after element 1 is a phone number")

Also, star syntax can be especially useful when iterating over
a sequence of tuples of varying length
"""
