def main():
    fileName = input("Enter file name: ")
    if fileName.lower().lstrip().rstrip().endswith(".jpg") or fileName.lower().lstrip().rstrip().endswith(".jpeg"):
        print("image/jpeg")
    elif fileName.lower().lstrip().rstrip().endswith(".pdf"):
        print("application/pdf")
    elif fileName.lower().lstrip().rstrip().endswith(".gif"):
        print("image/gif")
    elif fileName.lower().lstrip().rstrip().endswith(".png"):
        print("image/png")
    elif fileName.lower().lstrip().rstrip().endswith(".txt"):
        print("text/plain")
    elif fileName.lower().lstrip().rstrip().endswith(".zip"):
        print("application/zip")
    elif fileName.lower().lstrip().rstrip().endswith(".bin"):
        print("application/octet-stream")
    else:
        print("application/octet-stream")
main()
