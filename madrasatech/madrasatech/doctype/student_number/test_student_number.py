# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
import unittest
import frappe
from frappe.model.document import Document
from frappe import _, throw
from frappe.utils import random_string


from student_number import fill_students
class TestStudentNumber(unittest.TestCase):
    def test_students_count(self):
        students = frappe.db.sql("""select sgs.student, sgs.student_name, sg.program, sg.academic_year, sg.student_group_name
			from `tabStudent Group` sg
			LEFT JOIN  `tabStudent Group Student` sgs 
			ON sg.name=sgs.parent
            ORDER BY sgs.student_name
			""", as_dict=True)

        self.assertEqual(fill_students(self, "2022- 2023"), len(students))
