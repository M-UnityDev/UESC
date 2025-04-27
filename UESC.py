import re
import os
import mtranslate

global is_manual_mode

version = 1.0

def unicode_to_char(unicode_string):
    return chr(int(unicode_string[2:], 16)) if unicode_string.startswith("\\u") else unicode_string

def replace_unicode_in_quotes(match):
    original_string = re.sub(r'(\\u[0-9a-fA-F]{4})', lambda x: unicode_to_char(x.group()), re.sub('\n','',match.group()))

    if is_manual_mode:
        print("\nOrginal string: " + original_string)
        translated_string = mtranslate.translate(original_string,'en','auto')
        print("Translated string: " + translated_string)
        user_version = input("Enter the corrected version (Leave blank to leave the output unchanged) : ")

        if not user_version == '':
            translated_string = user_version
    else:
        translated_string = mtranslate.translate(original_string,'en','auto')
    
    return translated_string

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except:
        print("The path is not valid!")
        exit(1)
    
    global is_manual_mode 
    is_manual_mode = str.lower(input("Do you want to check and correct the output of translator? [y/n] : ")) == "y"
    if not is_manual_mode:
        print("Please Wait...")
    
    content_with_replaced_unicode = re.sub(r'"(.*?)"', replace_unicode_in_quotes, content, flags=re.DOTALL)
    return content_with_replaced_unicode

if __name__ == "__main__":
    print(f"UNICODE\nESCAPE\nSEQUENCE\nCATCHER\n{version}\n")
    file_path = input("Enter the path to the file: ")
    translated_content = process_file(file_path)
    file_name = os.path.join(os.path.dirname(file_path), f"{os.path.basename(file_path)}[TRANSLATED]")

    try:
        file = open(file_name, "x")
    except FileExistsError:
        if str.lower(input("\nFile Exists, Do you want to replace it? [y/n] : ")) == "y":
            file = open(file_name, "w")
        else:
            exit(126)

    file.write(translated_content)
    print(" ")
    print("Done")