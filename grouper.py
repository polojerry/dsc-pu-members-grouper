import csv


def csv_reader(csv_file):
    file_reader = csv.reader(open(csv_file, newline=''))
    return file_reader


def divide_multiple_selection(reader_file, area_of_interest, member_count=0):
    for member_row in reader_file:
        member_selections = member_row[4]
        member_selection = member_selections.split(";")

        for selection in member_selection:
            if selection == area_of_interest:
                member_count += 1
                print(area_of_interest + ": " + str(member_count))


if __name__ == "__main__":
    csv_file_path = "dsc_pu_members_list.csv"
    reader = csv_reader(csv_file_path)
    sorted_list = sorted(reader, key=lambda _row: _row[4], reverse=False)

    divide_multiple_selection(sorted_list, "Android Development")
