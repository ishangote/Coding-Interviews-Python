"""
Flatten a Dictionary
A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, 
Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. 
In simple terms, a dictionary is a collection of unique keys and their values. 
The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). 
However, for this exercise assume that values are either an integer, a string or another dictionary.
Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .
If a certain key is empty, it should be excluded from the output (see e in the example below).

Example:
input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, 
c and d the result key would be Key2.c.d.
"""
#Iterative
def flatten_nested_dict_iter(input_dict):
    ans = {}
    stack = [("", input_dict)]

    while stack:
        prev_key, cur_dict = stack.pop()

        for k in cur_dict:
            val = cur_dict[k]

            if type(val) is str:
                if not prev_key: ans[k] = val
                else: 
                    if k: ans[prev_key + '.' + k] = val  
                    else: ans[prev_key] = val
            
            else:
                if not prev_key: stack.append((k, val))
                else: stack.append((prev_key + '.' + k, val))

    return ans

#Recursive
def flatten_nested_dict_util(prev_key, cur_dict, ans):
    for k in cur_dict:
        val = cur_dict[k]
        if type(val) is str:
            if not prev_key: ans[k] = val
            else:
                if k: ans[prev_key + '.' + k] = val
                else: ans[prev_key] = val
        else:
            if not prev_key: flatten_nested_dict_util(k, val, ans)
            else: flatten_nested_dict_util(prev_key + '.' + k, val, ans)

def flatten_nested_dict_recur(input_dict):
    ans = {}
    flatten_nested_dict_util("", input_dict, ans)
    return ans

import unittest
class TestFlattenDictionary(unittest.TestCase):
    def test_pramp_iter(self):
        self.assertEqual(flatten_nested_dict_iter({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}), {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"})
        self.assertEqual(flatten_nested_dict_iter({"Key":{"a":"2","b":"3"}}), {"Key.a":"2","Key.b":"3"})
        self.assertEqual(flatten_nested_dict_iter({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}), {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"})
        self.assertEqual(flatten_nested_dict_iter({"":{"a":"1"},"b":"3"}), {"a":"1","b":"3"})
        self.assertEqual(flatten_nested_dict_iter({"a":"1"}), {"a":"1"})
        self.assertEqual(flatten_nested_dict_iter({"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}), {"a.b.c.d.e.f":"awesome"})
    
    def test_pramp_iter(self):
        self.assertEqual(flatten_nested_dict_recur({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}}), {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"})
        self.assertEqual(flatten_nested_dict_recur({"Key":{"a":"2","b":"3"}}), {"Key.a":"2","Key.b":"3"})
        self.assertEqual(flatten_nested_dict_recur({"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}}), {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"})
        self.assertEqual(flatten_nested_dict_recur({"":{"a":"1"},"b":"3"}), {"a":"1","b":"3"})
        self.assertEqual(flatten_nested_dict_recur({"a":"1"}), {"a":"1"})
        self.assertEqual(flatten_nested_dict_recur({"a":{"b":{"c":{"d":{"e":{"f":{"":"awesome"}}}}}}}), {"a.b.c.d.e.f":"awesome"})
        
if __name__ == "__main__": unittest.main()