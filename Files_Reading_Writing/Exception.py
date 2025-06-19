try:
    f = open('Curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print('IOError occurred:', e)
except Exception as e:
    print('Exception occurred:', e)
    f = open('example_file.txt', 'r')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')