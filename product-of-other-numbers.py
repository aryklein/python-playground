#!/usr/bin/python

# You have a list of integers, and for each index you want to find the product of every
# integer except the integer at that index.
#
# Write a function get_products_of_all_ints_except_at_index() that takes a list of
# integers and returns a list of the products.
#
# https://www.interviewcake.com/question/python/product-of-other-numbers

def get_products_of_all_ints_except_at_index(lst):
    print (lst)
    prod = 1
    prod_list = []

    for index in range(len(lst)):
        prod = 1
        for j in lst:
            if lst.index(j) is not index:
                prod *= j
            
        prod_list.append(prod)

    return (prod_list)


if __name__ == '__main__':
    lst = [1, 7, 1, 4]
    result = get_products_of_all_ints_except_at_index(lst)
    print('List of integers': lst)
    print('List of the products': result)
