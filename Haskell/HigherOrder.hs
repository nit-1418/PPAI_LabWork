-- Anime-themed power scale function
animePowerScale :: Integer -> Integer
animePowerScale level = level ^ 2  -- You can customize the power scale function

applyFunction :: (Integer -> Integer) -> [Integer] -> [Integer]
applyFunction _ [] = []
applyFunction f (x:xs) = f x : applyFunction f xs

main :: IO ()
main = do
    putStrLn "Anime Power Scale:"
    putStrLn "Enter a list of anime character power levels (comma-separated):"
    input <- getLine
    let powerLevels = map read (wordsWhen (== ',') input)
    let scaledPowerLevels = applyFunction animePowerScale powerLevels
    putStrLn $ "Original Power Levels: " ++ show powerLevels
    putStrLn $ "Scaled Power Levels: " ++ show scaledPowerLevels

-- Helper function to split input string into a list of words
wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s = case dropWhile p s of
    "" -> []
    s' -> w : wordsWhen p s''
        where (w, s'') = break p s'
