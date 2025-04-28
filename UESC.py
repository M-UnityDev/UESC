import re
import os
import mtranslate

global is_manual_mode

version = 1.1

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    WHITE = '\033[97m'
    YELLOW = '\033[93m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def unicode_to_char(unicode_string):
    return chr(int(unicode_string[2:], 16)) if unicode_string.startswith("\\u") else unicode_string

def replace_unicode_in_quotes(match):
    original_string = re.sub(r'(\\u[0-9a-fA-F]{4})', lambda x: unicode_to_char(x.group()), re.sub('\n','',match.group()))

    if is_manual_mode:
        print(f"\n{colors.GREEN}Orginal string: {colors.WHITE}{original_string}")
        translated_string = mtranslate.translate(original_string,'en','auto')
        print(f"{colors.BLUE}Translated string: {colors.WHITE}{translated_string}")
        user_version = input(f"{colors.RED}Enter the corrected version (Leave blank to leave the output unchanged) : {colors.DEFAULT}")

        if not len(str.strip(user_version," ")) == 0:
            translated_string = user_version
    else:
        translated_string = mtranslate.translate(original_string,'en','auto')
    
    return translated_string

def write_to_a_file(file_path, argument_to_open_with, content_to_write):
    with open(file_path, encoding='utf-8', mode=argument_to_open_with) as file:
        file.write(content_to_write)

def process_file(file_path):
    try:
        with open(file_path, encoding='utf-8') as file:
            content = file.read()
    except:
        print(f"{colors.RED}{colors.BOLD}The path is invalid!")
        exit(1)
    
    global is_manual_mode 
    is_manual_mode = str.lower(input("Do you want to check and correct the output of translator? [Y/N] : ")) == "y"
    if not is_manual_mode:
        print("Please Wait...")
    
    content_with_replaced_unicode = re.sub(r'"(.*?)"', replace_unicode_in_quotes, content, flags=re.DOTALL)
    return content_with_replaced_unicode

if __name__ == "__main__":
    print(f"\n{colors.BOLD}{colors.RED}UNICODE\n{colors.GREEN}ESCAPE\n{colors.BLUE}SEQUENCE\n{colors.WHITE}CATCHER\n\n{version}\n{colors.DEFAULT}")
    file_path = input(f"Enter the path to the file: {colors.UNDERLINE}")
    print(colors.DEFAULT)
    translated_content = process_file(file_path)
    file_name = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}[TRANSLATED]")

    try:
        write_to_a_file(file_name, "x", translated_content)
    except FileExistsError:
        if str.lower(input(f"\n{colors.YELLOW}File Exists, Replace it? [Y/N] : {colors.DEFAULT}")) == "y":
            write_to_a_file(file_name, "w", translated_content)
        else:
            exit(126)

    print(f"\n{colors.BOLD}{colors.GREEN}Done\n")