# this code fullfills both File Read & Write Challenge and Custom Exception Challenge
class EmptyFileError(Exception):
    pass

fileName = input("Enter the filename you want to read: ")

try:
    
    with open(fileName, "r") as file:
        content = file.read()
        

        if not content:
            raise EmptyFileError("⚠️ The file is empty!")
        
        print("\n📄 Original File Content:\n")
        print(content)


    modified_content = content.upper()


    new_file = "modified_" + fileName
    with open(new_file, "w") as file:
        file.write(modified_content)

    print(f"\nModified content has been saved to: {new_file}")


except FileNotFoundError:
    print("Error: File not found. Please check the filename.")

except EmptyFileError as e:
    print("Custom Error:", e)
