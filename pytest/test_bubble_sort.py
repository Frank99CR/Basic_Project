import pytest
from bubble_sort import bubble_sort


def test_bubble_sort_returns_sorted_list_correctly():
    
    #Arrange
    list_to_sort = [2,3,4,1,5]
    sorted_list = [1,2,3,4,5]

    #Act
    result = bubble_sort(list_to_sort)

    #Assert
    assert result == sorted_list



