# Write your solution here
students = int(input("How many students on the course? "))
des_groupsize = int(input("Desired group size? "))

groups = -(students // -des_groupsize)

print(f'Number of groups formed: {groups}')