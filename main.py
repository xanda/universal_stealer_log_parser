from racoon import extract_passwords, extract_passwords2
from racoon_cc_parser import process_cc, process_cc_v2
main_folder = "/path/to/folder"
output_folder = "/path/to/folder"
output_file = "Treated_passwords_racoon.txt"
output_file2 = "Treated_passwords_redline.txt"

process_cc(main_folder)
process_cc_v2(main_folder)
extract_passwords(main_folder, output_folder, output_file)
extract_passwords2(main_folder, output_folder,output_file2)