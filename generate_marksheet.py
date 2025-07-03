import csv
from fpdf import FPDF

# Step 1: Read CSV and calculate total & average marks
students = []

with open("marks_data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["Name"]
        maths = int(row["Maths"])
        science = int(row["Science"])
        english = int(row["English"])
        total = maths + science + english
        average = total / 3
        students.append({
            "name": name,
            "total": total,
            "average": round(average, 2)
        })

# Step 2: Generate PDF report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="Student Marksheet Report", ln=1, align="C")

pdf.ln(10)  # Line break
pdf.set_font("Arial", size=12)

for student in students:
    pdf.cell(200, 10, txt=f"{student['name']}: Total Marks = {student['total']}, Average = {student['average']}", ln=1)

# Step 3: Save PDF
pdf.output("marksheet_report.pdf")
print("✅ PDF report generated: marksheet_report.pdf")