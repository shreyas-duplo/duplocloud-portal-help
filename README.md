# DuploCloud help
This repository has all the helps which is rendered on the DuploCloud entity forms.
## Adding Help for form
1. Provide the name to your form if it does not exists in duplo-ui source code.
2. Create a new file in the forms directory with the name as ```<formname>.yml```.
3. Start adding help for form fields as key-value pair. Where key is the name of field and value is detailed description about the field.

## Commit changes
If you have made any kind of changes in the help, do not forgot to regenerate the "en.json" file with below command
```
python consolidate.py
```

You might have to install ```pyyaml``` python dependency before running above command.
```
pip install pyyaml
```
