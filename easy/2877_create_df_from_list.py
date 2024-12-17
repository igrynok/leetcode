from typing import List

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:

    ids = [student[0] for student in student_data]
    ages = [student[1] for student in student_data]

    return pd.DataFrame({"student_id":ids, "age":ages})