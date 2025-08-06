# utils/pdf_template.py

from fpdf import FPDF
import pandas as pd

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "HR Pulse View Report", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section_title(self, title: str):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def add_table(self, dataframe: pd.DataFrame):
        self.set_font("Arial", "B", 10)
        col_widths = [25] * len(dataframe.columns)

        # Header row
        for col_name in dataframe.columns:
            self.cell(30, 8, str(col_name), border=1)
        self.ln()

        self.set_font("Arial", size=9)
        # Data rows
        for _, row in dataframe.iterrows():
            for value in row:
                self.cell(30, 8, str(value), border=1)
            self.ln()
