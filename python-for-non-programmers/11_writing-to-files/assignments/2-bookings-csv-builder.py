records = {}
while True:
    sold = input("Enter product and units sold separated by a colon (eg. SKU: number): ")

    if sold == '':
        break
    
    sold = sold.split(':')

    sku = sold[0].strip()
    num_sold = sold[1].strip()

    records[sku] = int(num_sold)

with open('sales-report.csv', 'w') as outfile:
    for sku, num in records.items():
        outfile.write(str(sku) + ',' + str(num) + '\n')

