import rsdLibrary as lib

from fpdf import FPDF
import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu

def output_df_to_pdf(pdf, df: pd.DataFrame):

	# A cell is a rectangular area, possibly framed, which contains some text
	# Set the width and height of cell
	table_cell_width = 25
	table_cell_height = 6
	# Select a font as Arial, bold, 8
	pdf.set_font('Arial', 'B', 8)
		
	# Loop over to print column names
	cols = df.columns
	for col in cols:
		pdf.cell(table_cell_width, table_cell_height, col, align='C', border=1)
	# Line break
	pdf.ln(table_cell_height)
	# Select a font as Arial, regular, 10
	pdf.set_font('Arial', '', 10)
	# Loop over to print each data in the table
	for row in df.itertuples():
		for col in cols:
			value = str(getattr(row, col))
			pdf.cell(table_cell_width, table_cell_height, value, align='C', border=1)
		pdf.ln(table_cell_height)
        
def Export():
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font('Arial', 'B', 16)

	print(colored("Select one of the following stored shops:", "magenta"))
	terminal_menu = TerminalMenu(lib.ReadCsv())
	terminal_menu.show()
	path = terminal_menu.chosen_menu_entry
	df = lib.read(path)

	output_df_to_pdf(pdf, df)
	# 3. Output the PDF file
	pdf.output('fpdf_pdf_report.pdf', 'F')