# Issue with Loading Pyxel on macOS

Greetings, 

I am getting an exception when attempting to load the pyxel module. I have installed the library using

`$> pip install -U pyxel`

however, when attempting to load the library using

`$> python -m pyxel`
or 
`$> pyxel`

I get the following stack trace:

```
<fomatted stack trace here>
```

It looks to me like an issue in loading shared object files, but I'm not quite sure how to resolve. Any advice or suggestions would be appreciated.

#### Attempted Resolutions

I've tried uninstalling and reinstalling python (moving from 3.7 to 3.10) with the same issue occuring. 


#### Debug Details:
OS Version: <macOS version here>
Python Version: <python version here>
