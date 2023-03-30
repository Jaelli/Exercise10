correct_PIN = "3764"
guess = ""
attempt_count = 0
attempt_limit = 3
out_of_attempts = False

while guess != correct_PIN and not(out_of_attempts):
    if attempt_count < attempt_limit:
        print("Attempts remaining: ", int(attempt_limit - attempt_count))
        guess = input("Enter your PIN: ")
        attempt_count += 1
    else:
        out_of_attempts = True

if out_of_attempts:
    print("No more attempts, PIN locked")
else:
    print("PIN correct")
