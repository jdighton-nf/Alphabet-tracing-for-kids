import pdfkit

data = str()

with open('template.html', 'r') as template:
    data = template.read()

output = str()

# desire 20 columns
# 10x Upper Case, 10x Lower Case
# A - Z

letters = [i for i in range(0, 101)]

for letter in letters:
    output += '<tr>'
    for _ in range(10):
        output += f'<td><div class="monospace">{letter}</div></td>'

output = data.format(output)

printable = pdfkit.from_string(output, 'workbook.pdf')
