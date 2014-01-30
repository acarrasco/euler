#lang racket
(define (sub_vec a b)
  (match (list a b)
    [(list (list ax ay) (list bx by))
     (list (- ax bx) (- ay by))]))

(define (dot_product a b)
  (match (list a b)
    [(list (list ax ay) (list bx by))
     (+ (* ax bx) (* ay by))]))

(define (all_different a b c)
  (not (for/or ([pair (list (list a b) (list b c) (list c a))])
         (apply equal? pair))))

(define (is_right_triangle a b c)
  (and (all_different a b c)
       (= 0 (* (dot_product (sub_vec a c) (sub_vec b a))
               (dot_product (sub_vec b a) (sub_vec c b))
               (dot_product (sub_vec c b) (sub_vec a c))))
       #t))

(define (brute_force n)
  (/ (for/sum ([ax (in-range n)])
       (for/sum ([ay (in-range n)])
         (for/sum ([bx (in-range n)])
           (for/sum ([by (in-range n)])
             (if (is_right_triangle '(0 0) (list ax ay) (list bx by))
                 1
                 0))))) 2))

(display (brute_force 51))
