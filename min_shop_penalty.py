import pytest

def test_base_case():
    s = Solution()
    assert s.bestClosingTime('N') == 0
    assert s.bestClosingTime('Y') == 1

def test_all_n():
    s = Solution()
    assert s.bestClosingTime('NNNNN') == 0

def test_all_y():
    s = Solution()
    assert s.bestClosingTime('YYYY') == 4

def test_early_close():
    s = Solution()
    assert s.bestClosingTime('YYNY') == 2

def test_late_close():
    s = Solution()
    assert s.bestClosingTime('YYNYYY') == 6

def test_not_worth():
    s = Solution()
    assert s.bestClosingTime('NNNYNN') == 0

pytest.main()

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = 0
        best_count = 0
        best_idx = 0
        for idx, char in enumerate(customers):
            #breakpoint()
            if char == 'Y':
                count += 1
                if count > best_count:
                    best_count = count
                    best_idx = idx + 1
            else:
                count -= 1
        return best_idx