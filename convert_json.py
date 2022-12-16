import pytablewriter

def convert(filename, from_ext, to_ext):
    input_file = f"{filename}.{from_ext}"

    writer = pytablewriter.JsonTableWriter()
    writer.from_csv(input_file)

    with open(f"./src/components/matrix/{filename}.{to_ext}", "w") as f:
        writer.stream = f
        writer.write_table()

if __name__ == '__main__':
    convert("internships", "csv", "json")
