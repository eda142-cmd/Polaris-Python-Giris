import re

def main():
    # Processing Level 1
    extract_data("lvl1_dirty_data.txt", "lvl1_clean_contact_list.txt")
    # Processing Level 2
    extract_data("lvl2_dirty_data.txt", "lvl2_clean_contact_list.txt")

def extract_data(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            content = file.read()
            
        # Regex patterns:
        # Email: alphanumeric and some symbols before @, then domain
        # Phone: Supports various formats like (555) 555-5555 or 5555555555
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
        
        emails = re.findall(email_pattern, content)
        phones = re.findall(phone_pattern, content)
        
        with open(output_file, "w") as out:
            out.write("--- EMAILS ---\n")
            for email in emails:
                out.write(f"{email}\n")
            out.write("\n--- PHONE NUMBERS ---\n")
            for phone in phones:
                out.write(f"{phone}\n")
        
        print(f"Extraction successful: {output_file} created.")
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")

if __name__ == "__main__":
    main()
