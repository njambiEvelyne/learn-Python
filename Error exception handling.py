try:
   f= open('testfile.txt')
   # var = bad_var
except FileNotFoundError:
    print('Sorry the file does not exist')
except Exception:
    print("Sorry something went wrong!")