import time

wait_attempt = 1
max_attempt = 5
attempt = 0


while attempt < max_attempt:
    print("Your No of attempt", attempt + 1, "wait-time", wait_attempt)
    time.sleep(wait_attempt)
    attempt += 1


# while attempt < max_attempt:
#     print("Your No of attempt", attempt + 1, "wait-time", wait_attempt)
#     time.sleep(wait_attempt)  # Wait for the specified time
#     attempt += 1  # Increment attempt
