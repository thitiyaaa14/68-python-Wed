def main():
    infile = open('philosophers.txt','w')
    file_contents = infile.read()
    infile.close()
    print(file_contents)
    main()