disk = ['R15','R18','R16','L15','L16','L18']
size = [sizee for sizee in disk if '15' in sizee]
print(size)



line = [i for i in range(-50,51,10)]
print(line)



college ={'Harvard':'University ','Massachusetts':'Institute of Technology ', 'University':'Cambridge ','University2': ' Oxford ', 'University3': 'College London ','Stanford':' University ','California': ' Institute of Technology ','Princeton': ' University ','Yale':'University ','Columbia':' University ','University4': ' Chicago ','Imperial College':' London '}
name = [i[0]for i in college ]
print(name)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [n*n for n in nums]
print(squares)



matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)


a = [i**2 for i in range(10)]
print(a)

salam = ['3', '44', 'Jarima ', 'Tursunbek ', ' Robberto ']
aleykum = [i+'Vvaleykum Assalam' for i in salam if 'r'  in i]
print(aleykum)