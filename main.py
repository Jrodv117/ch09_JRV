def sales_report(sales):
    region_counter = 1
    for row in sales:
        print(f"{str(region_counter):9s}", end="")
        for item in row:
            print(f"{item:10,.2f} ", end="")
        print()
        region_counter += 1


def sales_by_region(sales):
    region_counter = 1
    total = 0
    sum_of_index = 0
    print("\nTotal Sales by region:")
    for row in sales:
        for index in row:
            sum_of_index += index
        total += sum_of_index
        print(f"Region {str(region_counter)}: {(sum_of_index):4,.2f}")
        region_counter += 1
    return total


def main():
    sales = [
        [1540.0, 2010.0, 2450.0, 1845.0],
        [1130.0, 1168.0, 1847.0, 1491.0],
        [1580.0, 2305.0, 2710.0, 1284.0],
        [1105.0, 4102.0, 2391.0, 1576.0],
    ]
    print("Sales Report\n")
    print(f"{'Region':16s} {'Q1':10s} {'Q2':10s} {'Q3':10s} {'Q4':10s}")
    sales_report(sales)
    sales_by_region(sales)


main()
