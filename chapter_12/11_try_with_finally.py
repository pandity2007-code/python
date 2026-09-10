def main():
    try:

        a=int(input("enter the number:"))
        print(a)
    except ValueError:
       
       print("Please enter a valid integer.")
    finally:
        print("i am inside finally")

main()        
   