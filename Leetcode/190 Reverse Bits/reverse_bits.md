# 190. Reverse Bits

## Problem Statement

> Reverse bits of a given 32 bits unsigned integer.
>
> Note:
>
> - Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
> - In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
>
> Follow up: If this function is called many times, how would you optimize it?

> Constraints:
> The input must be a binary string of length 32

## Examples

Example 1:

```
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

Example 2:

```
Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

## Solution

```
Example 1

Input:
n =
001001010
        ^
        * This bit should go to the 0 position of res

Initialize res
res = 000...0   * 32 0's

n =
001001010
    &   => Logic AND operation
000000001
---------
000000000

res = 0000....0000  * 0 needs to be put at 1st position
      ^


n =
001001010  =>  000100101    * Right shift by 1
                   &
               o00000000
               ---------
               000000010

res = 0000....0000  * 1 needs to be put at 2nd position
       ^

* Logic OR res with result left shifted by 32 - 2 positions

...

Output: 010100100
```
