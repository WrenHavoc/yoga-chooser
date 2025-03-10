This is designed to work with linux systems but should theoretically work on mac and other unix/unix-like environments.
Windows sytems (in theory) could run this, but it will be buggy and missing some features.
you could modify this to work on systems other than linux. modify the lines that use os.system and that should be it.
for example, on windows you would want to change `os.system("clear")` to`os.system("cls")`

This is just a school project.
I'm a software dev, not a gym teacher so the information this software provides could easily be wrong.
please do not use this program for medical advice, I'm not a doctor either. 
If you dislocate your shoulder because you messed up a pose, it's not my fault.

# ----------[Version 1.0.0-b.1]----------

version notes:
I might never actually update this. This is not at all something I would consider a full release.
I am considering making a full release, but I'd really only do that if I have nothing else to do.
If you (for some reason) want to pick up development, please, feel free to message me over XMPP.
This is an XMPP address, not an email address. If you try to email it, nothing will happen: wren@404.city

this is the barebones, basic version of the program. It has gone through alpha testing but not beta testing. 

(possible) future features:
  - full support for windows and mac
  - ability to add new poses
  - create full routine
  - built in explanation of poses
  - improved tui or possibly gui
  - installation script
  - uninstallation script

none of the above information is a terms of use and should not be treated as legal documentation.
