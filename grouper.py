import csv

list_of_members = []
list_of_area_of_interest = [
    "Action on Google",
    "Android Development",
    "Google Cloud Platform",
    "Machine Learning and Artificial Intelligence",
    "Web Development"
]


def csv_reader(csv_file):
    file_reader = csv.reader(open(csv_file, newline=''))
    return file_reader


def divide_members_by_their_selection(reader_file, area_of_interest):
    for member_row in reader_file:
        member_selection = member_row[4].split(";")

        for selection in member_selection:
            if selection == area_of_interest:
                list_of_members.append(member_row)


def create_groups_file(area_of_interest):
    return open(area_of_interest + " Groups.txt", "w+")


def divide_list_into_groups(members_list, group_sizes):
    for member in range(0, len(members_list), group_sizes):
        yield list_of_members[member:member + group_sizes]


def group_members(department_name, members_list, group_size):
    group_file = create_groups_file(department_name)
    members_groups = divide_list_into_groups(members_list, group_size)

    group_counter = 1
    for member_group in members_groups:
        student_counter = 1
        group_file.write("Group " + str(group_counter) + "\n")

        for member in member_group:
            group_file.write(
                str(student_counter) + ". " + member[1] +
                " ||" + " Contact: " + member[2] +
                " || " + " Level: " + member[5] +
                " || " + " Year of Study: " + member[3] +
                "\n")
            student_counter += 1

        group_file.write("\n")
        group_counter += 1


if __name__ == "__main__":
    csv_file_path = "dsc_pu_members_list.csv"
    reader = csv_reader(csv_file_path)
    sorted_list = sorted(reader, key=lambda _row: _row[4], reverse=False)

    for interest in list_of_area_of_interest:
        divide_members_by_their_selection(sorted_list, interest)
        group_members(interest, list_of_members)
        list_of_members = []
