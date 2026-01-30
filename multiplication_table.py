def main():
    # Outer loop for rows
    for i in range(1, 10):
        # Inner loop for columns
        for j in range(1, 10):
            # Using end="\t" for alignment (Tab space)
            print(f"{i * j}", end="\t")
        print() # New line after each row

if __name__ == "__main__":
    main()
