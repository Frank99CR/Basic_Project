import pytest
from bubble_sort import bubble_sort

list_to_sort = [5,3,4,2,1]


def test_bubble_sort_returns_sorted_list_correctly(list_to_sort):
    
    #Arrange
    sorted_list = [1,2,3,4,5]

    #Act
    result = bubble_sort(list_to_sort)

    #Assert
    assert result == sorted_list


