(defun roman-digit-value (v)
  (case v
    (#\M 1000)
    (#\D 500)
    (#\C 100)
    (#\L 50)
    (#\X 10)
    (#\V 5)
    (#\I 1)))

(defun roman-to-decimal-helper (rest prev acc)
  (if rest
      (let ((curr (car rest))
   (next (cdr rest)))
(if (> curr prev)
   (roman-to-decimal-helper next curr (- acc prev))
   (roman-to-decimal-helper next curr (+ acc prev))))
      (+ acc prev)))

(defun roman-to-decimal (roman)
  (roman-to-decimal-helper (map 'list #'roman-digit-value roman) 0 0))

(defun decimal-to-roman (n)
  (if (> n 4000)
      (concatenate 'string "MMMM" (decimal-to-roman (- n 4000)))
      (format nil "~@R" n)))

(print
 (with-open-file (stream "roman.txt")
   (loop for line = (read-line stream nil)
      until (eq line nil)
      sum (- (length line)
    (length (decimal-to-roman (roman-to-decimal line)))))))

