fibs = 1 : 2 : zipWith (+) fibs (tail fibs)

main = do
    let result = sum (takeWhile (< 4000000) (filter even fibs))
    print result
