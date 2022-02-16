import os
from buildast_new.hard import hard_build_ast


def input_to_latex_format(input_str):
    return map(
        lambda temp: temp + ['' for _ in range(max(map(lambda x: len(x), input_str)) - len(temp))],
        input_str
    ), max(
        map(lambda x: len(x),
        input_str)
    )


def generate_pdf(input_str):
    input_str, table_size = input_to_latex_format(input_str)
    hard_build_ast()
    with open("artifacts/hard.tex", "w") as text_file:
        text_file.write(
            f"\\documentclass{{article}}\n\\usepackage{{graphicx}}\n\\begin{{document}}\n"
            + f"\\begin{{center}}\n\\begin{{tabular}}{{{'|' + '|'.join(['c' for _ in range(table_size)]) + '|'}}} \n\\hline\n" \
           + '\n'.join(map(lambda x: ' & '.join(str(field) for field in x) + ' \\\\', input_str)) \
           + "\n\\hline\n\\end{tabular}\n\\end{center}\n"
            + "\\begin{center}\n\\includegraphics[scale=0.09]{artifacts/hard.png}\n\\end{center}\n"
            + "\\end{document}")


if __name__ == '__main__':
    generate_pdf([["cell1", "cell2", "cell3"], ["cell4", "cell5", "cell6"], ["cell7", "cell8", "cell9"]])
    os.system("pdflatex -halt-on-error -output-directory artifacts artifacts/hard.tex")
    os.system("rm artifacts/hard.aux artifacts/hard.log artifacts/hard.png")
