# Doctrine Folders

Folders are the top-level categorization of doctrines, e.g. *land*, *air* and *navy*, but you can also create a custom folder with any name. Each *Grand Doctrine* belongs to one folder.
 
## Script Example
```
land = { 
    allowed = { # If this trigger evaluates to False, the folder won't be available
        always = yes    
    }
    name = LOC_KEY
    tab_gfx = GFX
}
```