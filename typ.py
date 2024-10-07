import pyautogui as pg
import time

def remove_leading_spaces(code):
    # Split the code into lines
    lines = code.split('\n')
    # Remove leading spaces from each line
    clexed_lines = [line.lstrip() for line in lines]
    # Remove comments from each line
    clexed_lines = [line.split('#')[0] for line in clexed_lines]
    # Join the clexed lines back into a single string
    clexed_code = '\n'.join(clexed_lines)
    return clexed_code

ximal=('''import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Read initial value of N
            int N = scanner.nextInt();
            
            // Read number of queries
            int Q = scanner.nextInt();
            
            // Process each query
            for (int i = 0; i < Q; i++) {
                int queryType = scanner.nextInt();
                
                if (queryType == 1) { // N | X
                    int X = scanner.nextInt();
                    N |= X; // Perform bitwise OR
                } else if (queryType == 2) { // N & X
                    int X = scanner.nextInt();
                    N &= X; // Perform bitwise AND
                } else if (queryType == 3) { // N ^ X
                    int X = scanner.nextInt();
                    N ^= X; // Perform bitwise XOR
                } else if (queryType == 4) { // ~N
                    N = ~N; // Perform bitwise NOT
                } else {
                    System.out.println("Invalid query type: " + queryType);
                }
                
                // Print the result of N after each query
                System.out.println(N);
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}

''')

clexed_code = remove_leading_spaces(ximal)

time.sleep(5)
pg.write(clexed_code)
