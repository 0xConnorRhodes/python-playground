def numsort(numlist, oddfile, evenfile):
    with open(oddfile, 'w') as oddfile, open(evenfile, 'w') as evenfile:
        for num in numlist:
            if num % 2 == 0:
                oddfile.write(str(num) + '\n')
            else:
                evenfile.write(str(num) + '\n')

