-- Define the isPalindrome function using direct recursion
isPalindrome :: String -> Bool
isPalindrome [] = True          -- An empty string is a palindrome
isPalindrome [_] = True         -- A string with one character is a palindrome
isPalindrome (x:xs)
    | x == lastChar = isPalindrome middleChars
    | otherwise = False
    where
        lastChar = last xs
        middleChars = init xs

-- Main program
main :: IO ()
main = do
    putStrLn "Palindrome Checker"

    -- Prompt for a string
    putStrLn "Enter a string:"
    input <- getLine

    -- Check if the entered string is a palindrome
    let result = isPalindrome input

    putStrLn $ if result then "It's a palindrome!" else "It's not a palindrome."
