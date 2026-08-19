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

To solve this problem cleanly, our team implemented and evaluated two distinct programming paradigms:

#### Approach 1: Direct Mathematical Derivation
This approach is based on the fundamental algebraic equation of time:
<div align="center"> $\text{total seconds} = (\text{hours} \times 3600) + (\text{minutes} \times 60) + \text{seconds}$ </div>

From this formula, we mathematically derive each time unit component:
1. **Hours**: Since 1 hour equals 3,600 seconds, the number of completed hours is the integer quotient of the total seconds divided by $3600$: 
<div align="center"> $\displaystyle \text{hours} = \lfloor \dfrac{\text{total seconds}}{3600} \rfloor$ </div>
2. **Seconds**: The seconds component represents the remaining seconds that cannot form a whole minute. Thus, it is the remainder when the total seconds is divided by 60:
   <div align="center"> $\text{seconds} = \text{total seconds} \pmod{60}$ </div>
3. **Minutes**: Once we have isolated the `hours` and `seconds`, we can subtract their contributions from the `total_seconds`. The leftover value represents the total seconds contributed solely by whole minutes. Dividing this value by 60 yields our target minutes:
   <div align="center"> $\text{minutes} = \frac{\text{total seconds} - (\text{hours} \times 3600) - \text{seconds}}{60}$ </div>


#### Approach 2: Base-60 (Sexagesimal) Positional System
Standard time-keeping is fundamentally a **sexagesimal (base-60)** system. 

A time representation can be modeled as a base-60 number system where:
<div align="center"> $\text{total seconds} = \text{hours} \cdot 60^2 + \text{minutes} \cdot 60 + \text{seconds}$ </div>

We designed a **generalized base converter** (`decimal_to_any_base`) that translates any base-10 decimal integer into its positional representation in base $B$. By setting **$B = 60$**, the output digits mapped directly to our desired hours, minutes, and seconds.


