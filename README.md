## Tutorial 1: Seconds to Time Converter

### **Team Members**

* GOH YU-HSUEN, ERICA
* SEET HUI XIN
* TEO WOO HNG REANNE
* TRAN MINH HOANG

### Problem Statement

There are $86,400$ seconds in a day ($24 \times 60 \times 60$). Given a number in the range $1$ to $86,400$, output the current time as hours, minutes, and seconds on a $24$-hour clock.

* **Example:** $70,000$ seconds is $19$ hours, $26$ minutes, and $40$ seconds.

### Implementation (`solution.py`)

The solution is implemented in Python, leveraging integer division (`//`) and the modulo operator (`%`) to split the total seconds progressively into hours, minutes, and remaining seconds.

```python
def convert_seconds_to_time(total_seconds):
    if not 1 <= total_seconds <= 86400:
        print("Error: Input seconds must be between 1 and 86,400.")
        return None, None, None

    hours = total_seconds // 3600
    remainder_seconds = total_seconds % 3600
    minutes = remainder_seconds // 60
    seconds = remainder_seconds % 60
    
    return hours, minutes, seconds

if __name__ == "__main__":
    input_seconds = 70000
    hours, minutes, seconds = convert_seconds_to_time(input_seconds)
    if hours is not None:
        print(f"Input: {input_seconds:,} seconds")
        print(f"Output: {hours} hours, {minutes} minutes, and {seconds} seconds.")
