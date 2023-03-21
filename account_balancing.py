import pytest
from typing import List

def test_base_case():
    s = Solution()
    assert s.minTransfers([[0, 1, 0]]) == 0

def test_unequal_trade():
    s = Solution()
    assert s.minTransfers([[0, 1, 10]]) == 1

def test_equal_trade():
    s = Solution()
    assert s.minTransfers([[0, 1, 10], [1, 0, 10]]) == 0

def test_multi_user():
    s = Solution()
    assert s.minTransfers([[0,1,10],[2,0,5]]) == 2

pytest.main()

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        def _hash_ids(id1, id2):
            if id1 < id2:
                return f"{id1}x{id2}y", 1
            else:
                return f"{id2}x{id1}y", -1
        
        debts = {}
        for debter, debtee, amount in transactions:
            if amount < 1:
                continue
            #breakpoint()
            hash_id, flip = _hash_ids(debter, debtee)
            if hash_id in debts:
                debts[hash_id] += amount * flip
            else:
                debts[hash_id] = amount * flip
        #breakpoint()
        return len([debt for debt in debts.values() if debt != 0])