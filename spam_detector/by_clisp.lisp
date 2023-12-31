(defun is-spam (email)
  (let ((spam-keywords '("buy now" "limited time" "earn money" "click here" "subscribe" "click below" "order now" "money back"
                          "free" "offer" "discount" "trial" "winner" "prize" "congratulations" "dear friend" "hello" "dear" "hello dear" "dear sir" "dear madam"
                          "dear customer" "dear winner" "dear lucky" "dear selected" "dear account" "dear email")))
    (some (lambda (keyword) (search keyword (string-downcase email))) spam-keywords)))

(defun check-email ()
  (format t "Enter your email: ")
  (let ((input-email (read-line)))
    (if (is-spam input-email)
        (format t "This email is likely spam.~%")
        (format t "This email is not spam.~%"))))

(check-email)
