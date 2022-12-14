import locale as lc

lc.setlocale(lc.LC_ALL, "en_us")


def sales_report(sales):
    region_counter = 1
    for row in sales:
        print(f"{str(region_counter):12s}", end="")
        for item in row:
            # print(f"{item:10,.2f} ", end="")
            print(f"{lc.currency(item, grouping=True)} ", end="")
        print()
        region_counter += 1


def sales_by_region(sales):
    region_counter = 1
    total = 0
    print("\n\nTotal Sales by region:")
    for row in sales:
        sum_of_index = 0
        for index in row:
            sum_of_index += index
        total += sum_of_index
        print(
            f"Region {str(region_counter)}: {lc.currency(sum_of_index, grouping=True)}"
        )
        region_counter += 1
    return total


def sales_by_quarter(sales):
    print("\nTotal Sales by quarter: ")
    quarter_sales_array = [0, 0, 0, 0]
    quarter_counter = 1

    for row in range(len(sales)):
        for i in range(len(sales[row])):
            quarter_sales_array[i] += sales[row][i]
    for row in range(len(quarter_sales_array)):
        print(
            f"Q{(quarter_counter)}: {lc.currency(quarter_sales_array[row], grouping=True)}"
        )
        quarter_counter += 1


def main():
    sales = [
        [1540.0, 2010.0, 2450.0, 1845.0],
        [1130.0, 1168.0, 1847.0, 1491.0],
        [1580.0, 2305.0, 2710.0, 1284.0],
        [1105.0, 4102.0, 2391.0, 1576.0],
    ]
    print("Sales Report\n")
    print(f"{'Region':18s} {'Q1':9s} {'Q2':9s} {'Q3':9s} {'Q4'}")
    sales_report(sales)
    grand_total = sales_by_region(sales)
    sales_by_quarter(sales)
    print(
        f"\nTotal annual sales, all regions: {lc.currency(grand_total, grouping=True)}"
    )


main()
