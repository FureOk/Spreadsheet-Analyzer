import csv


# Task 1 - Read the data from the spreadsheet
def read_data():
    sales_data = []

    with open('sales.csv', 'r') as sales_csv:
        sales_report = csv.DictReader(sales_csv)

        for row in sales_report:
            sales_data.append(row)

    return sales_data


def sales():
    data = read_data()

# 2 -  Collect all the sales from each month into a single list

    sales_list = []
    results = []

    for row in data:
        sale = int(row['sales'])
        month = row['month']
        expenses = int(row['expenditure'])

        result = {
            'sale': sale,
            'month': month,
            'expenses': expenses
        }

        results.append(result)

        sales_list.append(sale)

# Calculating the profit and loss of each month as percentages

    for result in results:
        difference = result.get('sale') - result.get('expenses')
        percentage = difference * 100
        if percentage > 0:
            print('For the month of {}: You had a {}% profit.'.format(result.get('month'), percentage))
        else:
            print('For the month of {}: You had a {}% loss.'.format(result.get('month'), percentage))

# Printing out the months with the highest and lowest sales

        if result.get('sale') == min(sales_list):
            print('The month of {} had the lowest sales: {} naira.'.format(result.get('month'), result.get('sale')))
        elif result.get('sale') == max(sales_list):
            print('The month of {} had the highest sales: {} naira.'.format(result.get('month'), result.get('sale')))
        else:
            print('')

# 3 - Output the total sales across all months

    total_sales = int(sum(sales_list))
    print('Total sales for the year is {} naira,'.format(total_sales))
    print()

# Calculating the estimate average sales made each month throughout the year
    average_sales = total_sales / 12
    print('Average sales for the year is {} naira a month'.format(int(average_sales)))

# Asking the User if they would like a summary of the results

    reply = input('Would you like to have a summary of the results. Yes/No? ')

    if reply == 'Yes' or reply == 'yes':

        # Output of the summary of the results to another file

        field_names = ['Total Sales', 'Average Sales', 'Lowest Sales', 'Highest Sales']

        sales_data = [
            {'Total Sales': total_sales, 'Average Sales': average_sales, 'Lowest Sales': min(sales_list),
             'Highest Sales': max(sales_list)}

        ]

        with open('output.csv', 'w+') as spreadsheet:
            spreadsheet = csv.DictWriter(spreadsheet, fieldnames=field_names)

            spreadsheet.writeheader()
            spreadsheet.writerows(sales_data)

    else:
        print('\n Press any key to exit.')


sales()
