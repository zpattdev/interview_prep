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

def test_exclude_positive_balance():
    s = Solution()
    assert s.minTransfers([[0,1,10],[1,0,1],[1,2,5],[2,0,5]]) == 1

pytest.main()

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        balances = {}
        for debter, debtee, amount in transactions:
            if debter not in balances:
                balances[debter] = amount * -1
            else:
                balances[debter] -= amount
            
            if debtee not in balances:
                balances[debtee] = amount
            else:
                balances[debtee] += amount
        
        return len([bal for bal in balances.values() if bal < 0])

    def minTransfersBalance(self, transactions: List[List[int]]) -> int:
        #attempt to perfectly balance all accounts (all have zero)
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