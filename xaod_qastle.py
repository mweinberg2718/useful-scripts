my_file = open('xaod_branches.txt', 'r')
collections = []
print("(call ResultTTree (call Select (call Select (call EventDataset (list 'localds:bogus')) (lambda (list e) (list")
for line in my_file:
    collection = line.split('.')[0]
    if not collection in collections:
        print("(call (attr e '", collection, "') '", collection, "')'", sep='')
        collections.append(collection)
print("))) (lambda (list e) (list")

my_file.seek(0)
for line in my_file:
    subscript = collections.index(line.split('.')[0])
    col_name = line.split('.')[0].lower()
    attribute = line.split('.')[1].rstrip()
    print("(call (attr (subscript e ", subscript, ") 'Select') (lambda (list ", col_name,
          ") (call (attr ", col_name, " '", attribute, "'))))", sep='')
print ("))) (list")

my_file.seek(0)
for line in my_file:
    out_name = line.split('.')[0].lower() + '_' + line.split('.')[1].rstrip()
    print("'", out_name, "'", sep='')
print(") 'forkme' 'dude.root')")
