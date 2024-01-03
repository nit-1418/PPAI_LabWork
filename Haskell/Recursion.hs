factorial :: Integer -> Integer
factorial 0 = 1
factorial n
    | n > 0 = n * factorial (n - 1)
    | otherwise = error "Factorial is undefined for negative numbers"

main :: IO ()
main = do
    putStrLn "Calculating factorial:"
    putStrLn "Enter a non-negative integer:"
    n <- readLn
    let result = factorial n
    putStrLn $ "Factorial: " ++ show result
