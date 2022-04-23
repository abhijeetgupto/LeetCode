# Write your MySQL query statement below
Select event_day as day,
       emp_id,
       Sum(out_time-in_time) as total_time
from Employees
group by 1,2;