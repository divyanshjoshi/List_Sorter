import csv

def get_data():
    entries = {}
    with open('hackathon_list.csv') as csvfile:
        reader  = csv.reader(csvfile)
        next(reader,None)

        for row in reader:
            entries[row[0]] = row[1]
    return entries

def sort_list(arr): 
    for i in range(1, len(arr)): 
        key = arr[i].lower() 
        j = i-1
        while j >=0 and key < arr[j].lower() : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    return  arr

if __name__ == "__main__":

    data = get_data()
    sorted_names = sort_list(list(data.keys()))
    print(sorted_names)
