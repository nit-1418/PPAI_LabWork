animePowerScale :: Integer -> Integer -> Integer
animePowerScale base exp
    | exp == 0 = 1
    | exp == 1 = base
    | exp == 2 = base ^ 2
    | exp == 3 = base ^ 3
    | exp == 4 = base ^ 4
    | otherwise = base ^ exp  -- For exponents greater than 4, use the regular calculation

animeCalculatePower :: Integer -> Integer -> Integer
animeCalculatePower base exp = animePowerScale base exp

main :: IO ()
main = do
    putStrLn "Calculating anime power:"
    putStrLn "Enter the base:"
    base <- readLn
    putStrLn "Enter the anime power level (exponent):"
    exp <- readLn
    let result = animeCalculatePower base exp
    putStrLn $ "Result: " ++ show result
