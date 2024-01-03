fibEven :: Integer -> Integer
fibEven 0 = 0
fibEven 1 = 1
fibEven n = fibOdd (n - 1) + fibOdd (n - 2)

fibOdd :: Integer -> Integer
fibOdd 0 = 1
fibOdd 1 = 1
fibOdd n = fibEven (n - 1) + fibEven (n - 2)

main :: IO ()
main = do
    putStrLn "Fibonacci Sequence Generator"
    putStrLn "Enter the value of n:"
    n <- readLn
    let fibonacciSequence = [fibEven i | i <- [0..n-1]]
    putStrLn $ "Fibonacci Sequence up to the " ++ show n ++ "th term: " ++ show fibonacciSequence
