import time

def stopwatch():
    print("Press Enter to start, and Ctrl+C to stop.")
    input()
    start_time = time.time()

    try:
        while True:
            elapsed_time = time.time() - start_time
            formatted_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            print(f"\rElapsed Time: {formatted_time}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")

stopwatch()
