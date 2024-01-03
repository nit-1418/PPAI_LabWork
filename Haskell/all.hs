-- Define the pure functions

calculatePower :: Integer -> Integer -> Integer
calculatePower _ 0 = 1
calculatePower base exp
    | exp > 0 = base * calculatePower base (exp - 1)
    | otherwise = error "Exponent must be non-negative"

factorial :: Integer -> Integer
factorial n
    | n >= 0 = product [1..n]
    | otherwise = error "Input must be non-negative"

applyFunction :: (Integer -> Integer) -> [Integer] -> [Integer]
applyFunction _ [] = []
applyFunction f (x:xs) = f x : applyFunction f xs

-- Main program

main :: IO ()
main = do
    putStrLn "Haskell Program with Anime Power Scale:"
    
    -- Prompt for base and exponent
    putStrLn "Enter the base:"
    base <- readLn
    putStrLn "Enter the exponent:"
    exp <- readLn
    let powerResult = calculatePower base exp
    putStrLn $ "Result of raising base to exponent: " ++ show powerResult
    
    -- Prompt for non-negative integer
    putStrLn "Enter a non-negative integer:"
    integerInput <- readLn
    let factorialResult = factorial integerInput
    putStrLn $ "Factorial of the entered integer: " ++ show factorialResult
    
    -- Prompt for a list of integers
    putStrLn "Enter a list of integers (comma-separated):"
    listInput <- getLine
    let inputList = map read (wordsWhen (== ',') listInput)
    
    -- Apply the anime power scale to each element in the list
    let scaledList = applyFunction animePowerScale inputList
    
    putStrLn $ "Original List: " ++ show inputList
    putStrLn $ "Scaled List: " ++ show scaledList

-- Anime-themed power scale function
animePowerScale :: Integer -> Integer
animePowerScale level = level ^ 2

-- Helper function to split input string into a list of words
wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'
