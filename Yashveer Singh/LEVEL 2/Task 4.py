def fibonacci(n):
   
   sequence = []
   for i in range(n):
      if i == 0:
         sequence.append(0)
      elif i == 1:
         sequence.append(1)
      else:
         sequence.append(sequence[i - 1] + sequence[i - 2])
         
   return sequence
    
def main():
        """Generates the fibonacci sequence up to a given number of  terms."""

        n = int(input("Enter the number of terms:"))
        sequence = fibonacci(n)
        print("The fibonacci sequence up to {} terms is: {}".format(n, sequence))

if __name__ == "__main__":
    main()