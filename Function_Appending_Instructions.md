## Documentation for Other Developers: Appending a Function to the Logging Dictionaries

---

Once you have implemented a new SpectraGuru function or algorithm, you must perform the following steps to ensure that a) users have direct access to the relevant references and documentation for that function, and b) SpectraGuru can keep track of and display how many times that function has been called over the application's history.

In summary, your function needs a *keyname*, *readable name*, and *reference mapping*, which must be manually determined by the developer. Please follow the steps below to complete this process:

1. Determine a keyname for your function/algorithm. By convention, keynames take the form 'DOMAIN_FEATURE_ALGORITHM', with underscores used to separate words (Example: 'Processing_Normalization_Area').
	- DOMAIN is almost always 'Processing' or 'Analytics'
	- FEATURE is the high-level problem your algorithm is meant to solve (i.e. Normalization)
	- ALGORITHM is the name of the specific implementation of this solution (i.e. Area_Normalization)
	- FEATURE and ALGORITHM may be the same if appropriate. In this case, the keyname takes the form 'DOMAIN_FEATURE'.
	- See the existing keynames in `function_dict.py` for further reference.
2. In the Streamlit page file (i.e. `3_Processing.py` or `4_Analytics.py`) where your function is called, make sure that `log.log_function_call(f_name, f_params)` is invoked correctly for when the function is used. This increments the function usage counter.
	- In the Processing page, `log.log_function_call()` should be invoked when the user presses the 'Process' button if the target function was part of the user's selection.
	- In the Analytics page, `log.log_function_call()` should be invoked after the associated diagrams/graphs have been drawn.
	- `log.log_function_call()` takes two parameters. `f_name` is your function's keyname. `f_params` should be a dictionary containing the parameters the user used when calling your function. There are no hard constraints on the entries of this dictionary; feel free to only include parameters you deem to be important, or even pass an empty dictionary.
	- See the existing implementation for further reference or ask for assistance.
3. Open `function_dict.py`. You will need to add some entries to the three dictionaries stored there. The first dictionary is called `names`. The purpose of `names` is to translate your function keyname into user-readable Feature and Algorithm names.
	- For a new entry in the dict, the key is your function keyname, and the value is a 2-tuple of user-readable strings `("[Feature]","[Algorithm]")`. These strings will be displayed in the function usage table towards the bottom of the SpectraGuru welcome page. Just like with the keyname itself, `[Feature]` and `[Algorithm]` may be the same if appropriate.
4. The second dictionary is called `references`. This dictionary contains all the references to research papers, documentation, etc. used by SpectraGuru. If you need to add a reference to this list, use one of the empty templates towards the bottom of the dict.
	- `"text"` is either a raw string of text or a link to a reference. If a link, set `"link"` to `True`.
	- `"link"` is `True` if the content of `"text"` is a link, and `False` otherwise. Be sure to replace its default value of `None` when filling an entry.
	- `"doc_page"` is `True` if the link contained in `"text"` is a link to a page on SpectraGuru's documentation website, and `False` otherwise. Be sure to replace its default value of `None` when filling an entry.
	- `"notes"` can be anything (it is not used by the application), but ideally it should provide some information to other developers about what this reference is for.
	- *Important: Never change the numbers keying the existing entries in this dictionary.* The next dictionary uses these numbers.
5. The third dictionary is called `reference_map`. Its purpose is to map functions to their relevant references via a list of numbers, which represent rows in the `references` dict.
	- Use the function keyname as the key.
	- The value is an array of numbers corresponding to rows in the `references` dict. Simply list which references you want to be linked to this function.
	- `0` corresponds to "self-implemented," meaning that SpectraGuru developers implemented this function on their own without using existing libraries or outside research. Make sure `0` is the first element of the array if it is included at all.
	- Try not to map functions to more than five references unless necessary; this could clutter the function usage table.

*If you are appending a function to `function_dict.py` and are unsure of how to format your entry, use the existing entries as a guide or ask for clarification if necessary. All feedback is appreciated.*