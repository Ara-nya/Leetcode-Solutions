class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Step 1: Count consecutive matching characters
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Step 2: Write the character
            chars[write] = char
            write += 1
            
            # Step 3: If count > 1, write each digit of the count
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
                    
        return write