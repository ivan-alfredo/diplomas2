import csv
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os


def read_names():
    print(f'[INFO] reading names')
    person_data = []
    with open('names.txt', newline='') as csv_file:
        reader = csv.reader(csv_file, skipinitialspace=True)
        for row in reader:
            person_data.append(row)
    return person_data


def read_xml():
    print(f'reading XML file')
    with open('graphics.svg') as xml_file:
        template0 = "<tspan font-family=\"Comfortaa\" font-size=\"16\" "
        template1 = "font-weight=\"700\" fill=\"black\" x=\"0\" y=\"14\">"
        template2 = "</tspan>"
        template = template0 + template1 + "Nombre" + template2
        # print("printin template")
        # print(template)
        svg_txt = []
        beginning = ""
        for line in xml_file:
            if template in line:
                print("o noes i found it but donno what to do with it")
                svg_txt.append(beginning)
                svg_txt.append(template0)
                svg_txt.append(template1)
                svg_txt.append(template2)
                beginning = ""
                continue
            beginning += line
        svg_txt.append(beginning)
    return svg_txt


def insert_names(svg_txt, name1, name2):
    # refactr me with more data
    print(f'[INFO] replacing names')
    return svg_txt[0] + svg_txt[1] + svg_txt[2] + name1 + name2 + svg_txt[3] + svg_txt[4]


def generate_svgs_strings(svg_txt, ppl_data):
    all_svg_txts = []
    for row in ppl_data:
        all_svg_txts.append(insert_names(svg_txt, row[0], row[1]))
    return all_svg_txts


def write_pdf(some_txt):
    print(f'printin 1 of 100')
    # write the svg txt...this is outrageous but svg2rlg wont accept a string
    with open('tmp.svg', 'w') as temp_file:
        temp_file.write(some_txt)
    drawing = svg2rlg("tmp.svg")
    if os.path.exists("tmp.svg"):
        os.remove("tmp.svg")
    else:
        print("[WARN] SVG temp file does not exist")
    renderPDF.drawToFile(drawing, "file.pdf")


if __name__ == '__main__':
    names_array = read_names()
    svg_file = read_xml()  # svg_file is the svg in mem
    # print(insert_names(svg_file, "Candelaria", "Andrea"))
    full_txts = generate_svgs_strings(svg_file, names_array)
    print(full_txts[4])
    write_pdf(full_txts[4])

