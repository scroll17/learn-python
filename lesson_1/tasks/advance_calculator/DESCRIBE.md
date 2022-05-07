# Advance calculator

**You must realize logic which is equal to sample below.**

**Supported operators:**
- `+`
- `-`
- `*`
- `/`
- `()`
- `!`

## 1. Expected behavior

```text
>>> expression: 1 + 2 + 3
>>> result: 6
>>> expression: (4 - 2) + 3
>>> result: 5
>>> expression: 2 * 3 + 3
>>> result: 6
>>> expression: (8 / 2) * 3
>>> result: 12
>>> expression: 7!
>>> result: 5040
>>> action: exit
>>> calculator terminated....
```

## 2. Explain of work logic 

It's realization means that you need write a parser which can correctly parse expression and can understand priority. 