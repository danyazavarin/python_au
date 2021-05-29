import random
import datetime
import math
from itertools import chain

def generate_counts_by_cos(n):
    x_data = [i*(math.pi/n) for i in range(n)]
    return [str(int(10 + 40*math.cos(x))) for x in x_data]
  
def generate_data_by_line(n):
    k = random.randint(-2,2)
    return [30 + k*x for x in range(n)]

def generate_counts_by_pow(n):
    return [str(int((2 ** i)*10)) if 2**i < 10 else str(int((2**i))) if 2**i < 100 else str(int((2**i)/10)) if 2**i<1000 else str(int((2**i)/100)) for i in range(n)]

def generate_dates(n):
    start = datetime.datetime(2020, 1, 6)
    return [(start + datetime.timedelta(days=i * 30)).strftime('%Y-%m') for i in range(n)]

def generate_resources(n):
    return [str(random.randint(1, 3)) for i in range(n)]

def generate_staff_ids(n):
    return [str(random.randint(20, 25)) for i in range(n)]

def generate_data_and_write(n, file_name, resource_number, staff_id=0): 
    if (staff_id < resource_number and staff_id != 0) or resource_number <= 0:
        print('some resources do not exist')
        return
    functions = [generate_counts_by_sin, generate_counts_by_pow, generate_counts_by_log]
    all_data = []
    data = []
    for i in range(resource_number):
        data.append(functions[i % (len(functions))](n))
    dates = generate_dates(n)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = dates[j] + ', ' + str(i+1) + ', ' + data[i][j]
    data = list(chain.from_iterable(data))
    data2 = data.copy()

    if staff_id != 0:
        staff_dict = {i: [] for i in range(1, staff_id + 1)}
        while len(data2) != 0:
            worker = random.randint(1, staff_id)
            if len(staff_dict[worker]) != 12:
                num_of_month = random.randint(0, len(data2)-1)
                month = data2[num_of_month]
                if month[:7] not in staff_dict[worker]:
                    staff_dict[worker].append(month[:7])
                    all_data.append(data2[num_of_month] + ', ' + str(worker) + '\n')
                    data2.pop(num_of_month)
        all_data.insert(0, 'date, resource, count, staff_id\n')
    else:
        all_data = data.copy()
        for row in all_data:
            row += '\n'
        all_data.insert(0, 'date, resource, count\n')
    file = open(file_name, 'w')
    for i in all_data:
        file.write(i)
    file.close() 
