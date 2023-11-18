"""
Given a list of [FileName, FileSize, [Collection]] - Collection is optional, i.e., a collection can have 1 or more files. Same file can be a part of more than 1 collection.
How would you design a system

    To calculate total size of files processed.
    To calculate Top K collections based on size.
    Example:

file1.txt(size: 100)
file2.txt(size: 200) in collection "collection1"
file3.txt(size: 200) in collection "collection1"
file4.txt(size: 300) in collection "collection2"
file5.txt(size: 100)

Output:

Total size of files processed: 900
Top 2 collections:
- collection1 : 400
- collection2 : 300
"""
from collections import defaultdict
def do_processing(llist):
    total_file_size = 0
    collections = defaultdict(lambda: 0)
    for l in llist:
        size = len(l)
        file_name = l[0]
        file_size = l[1]
        if size > 2:
            collections = l[2:]

        for collection in collections:
            collections[collection] += file_size
        total_file_size += file_size
        collections = sorted(collections.items(), lambda _c, s: s)

    
        