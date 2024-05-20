import os

current_directory = os.path.dirname(os.path.abspath(__file__))
addresses_file_path = os.path.join(current_directory, 'adresses.txt')

with open(addresses_file_path, 'r') as file:
    addresses_to_compare = [line.strip() for line in file.readlines()]

address_points = {}

for filename in os.listdir(current_directory):
    if filename.endswith('points.txt'):
        points = int(filename.split('points')[0])
        filepath = os.path.join(current_directory, filename)

        with open(filepath, 'r') as file:
            addresses = file.readlines()
            for address in addresses:
                address = address.strip()
                if address in addresses_to_compare:
                    if address in address_points:
                        address_points[address] += points
                    else:
                        address_points[address] = points

result_file_path = os.path.join(current_directory, 'result.txt')
with open(result_file_path, 'w') as file:
    for address, points in address_points.items():
        file.write(f'{address}: {points}\n')

print("Все адреса успешно обработаны и сохранены в result.txt")
