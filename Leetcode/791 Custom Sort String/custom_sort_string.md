# 791. Custom Sort String

## Problem Statement

> You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
> Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
> Return any permutation of s that satisfies this property.

> Constraints:
>
> - 1 <= order.length <= 26
> - 1 <= s.length <= 200
> - order and s consist of lowercase English letters.
> - All the characters of order are unique.

## Examples

Example 1:

```
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.
```

Example 2:

```
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.
```

## **Custom Sort String Implementation Summary**

### **Approach**

The problem requires sorting string `s` based on the order specified in `order`, while keeping the relative order of characters **not in `order`** unchanged.

---

### **Design**

1. **Frequency Count (`Counter`)**:

   - Count occurrences of each character in `s`.
   - This helps efficiently construct the sorted string.

2. **Constructing Result String (`res`)**:
   - **Step 1**: Append characters from `order` based on their frequency in `s` and remove them from the counter.
   - **Step 2**: Append remaining characters from `s` in their original order.

---

### **Complexity Analysis**

- **Time Complexity**:
  - `O(n + m)`, where `n = len(s)` and `m = len(order)`.
  - `O(n)` to build the frequency map.
  - `O(m)` to process characters in `order`.
  - `O(n)` to append remaining characters.
  - **Overall: O(n + m)**
- **Space Complexity**:
  - `O(n)`, storing frequency map and result string.

---

### **Key Steps**

1. **Build frequency count of `s`** → `O(n)`.
2. **Append characters from `order`** (if present in `s`) → `O(m)`.
3. **Append remaining characters** in `s`'s original order → `O(n)`.
4. **Return final result string**.

---
