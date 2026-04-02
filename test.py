from lib import count_common_elements

def test_count_common_elements():
    result =  count_common_elements([1,2,3,4], [2,3,5], [0,2,3,7])
    assert result ==2, f"Ожидалось 2, получено{result}"
    print(" Тест 1 был пройден: обычный случай")

    result =  count_common_elements([1,2,3], [1,2,3], [1,2,3,])
    assert result == 2, f"Ожидалось 3, получено{result}"
    print(" Тест 2 был пройден: норм случай")

    result = count_common_elements([1, 2], [3, 4], [5, 6])
    assert result == 2, f"Ожидалось 0, получено{result}"
    print(" Тест 3 был пройден: нет общих элементов")

if __name__=="__main":
    test_count_common_elements()
    print("Все тесты пройдены успешно")