def d_mean(x):
    sum = 0
    count = 0
    for item in x:
        sum += item
        count += 1
    return sum / count

def d_median(x):
    x.sort()
    if len(x) % 2 == 0:
        middle_index = int(len(x) / 2)
        num_1 = x[middle_index]
        num_2 = x[middle_index + 1]
        median = (num_1 + num_2) / 2
        return median
    else:
        middle_index = int((len(x) + 1 ) / 2)
        median = x[middle_index]
        return median

def d_mode(x):
    count_high = 0
    count_num = 0
    for num in x:
        if count_high < x.count(num):
            count_high = x.count(num)
            count_num = num
    if count_high == 0 or count_high == 1:
        return 0
    else:
        return count_num


def d_range(x):
    x.sort()
    min_value = x[0]
    max_value = x[-1]
    return max_value - min_value


dataset_1 = [90, 98, 96, 96, 96, 98, 95, 94, 94, 91]
dataset_2 = [90, 98, 96, 94, 86, 88, 85, 90, 90, 95]
dataset_3 = [80, 88, 86, 86, 89, 92, 92, 91, 90, 91]

print("DATASET 1")
print("Mean:", d_mean(dataset_1))
print("Median:", d_median(dataset_1))
print("Mode:", d_mode(dataset_1))
print("Range:", d_range(dataset_1))

print("DATASET 2")
print("Mean:", d_mean(dataset_2))
print("Median:", d_median(dataset_2))
print("Mode:", d_mode(dataset_2))
print("Range:", d_range(dataset_2))

print("DATASET 3")
print("Mean:", d_mean(dataset_3))
print("Median:", d_median(dataset_3))
print("Mode:", d_mode(dataset_3))
print("Range:", d_range(dataset_3))