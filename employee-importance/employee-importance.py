"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        count = 0
        sub_id = []
        
        for employee in employees:
            if employee.id == id :
                count += employee.importance
                sub_id = employee.subordinates
                employees.remove(employee)
                break
        
        while sub_id :
            new = []
            for id in sub_id :
                for employee in employees :
                    if employee.id == id:
                        count += employee.importance
                        new += employee.subordinates
                        employees.remove(employee)
                        break
            sub_id = new
        return count
            
                    
            
            
            
            
            
        