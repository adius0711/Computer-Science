from os import read
import pickle


objects = []
# with (open(r"C:\Users\ashwi\Downloads\CSE 535 Information Retrieval\CSE_4535_Fall_2021-master\CSE_4535_Fall_2021-master\project4\data\poi_1.pkl", "rb")) as openfile:
#     while True:
#         try:
#             objects.append(pickle.load(openfile))
#         except EOFError:
#             break

# for i in range(len(objects)):
#   print(objects[i])


# print(objects[1])
readFile = open(r"C:\Users\ashwi\Downloads\CSE 535 Information Retrieval\CSE_4535_Fall_2021-master\CSE_4535_Fall_2021-master\project4\data\poi_1.pkl",  "rb")
dictionary = pickle.load(readFile)
# print(dictionary[id])
# keys = dictionary.keys()
# for id in dictionary.keys():
#     print(id, '->', dictionary[id])
with open(r"C:\Users\ashwi\Downloads\CSE 535 Information Retrieval\CSE_4535_Fall_2021-master\CSE_4535_Fall_2021-master\project4\data\poi_1.pkl", 'rb') as f:
    b = pickle.load(f)
    all_id = []
    for id in b:
        all_id.append(b['id'])
        # print(b['id'])
    # print(b.poi_name)
    print(all_id[1])