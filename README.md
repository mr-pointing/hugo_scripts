## Hugo Scripts

The scripts I run to get my Obisidian notes prepped for my [website](https://mrpointing.com). Big thanks to 
[`obsidian-to-hugo`](https://github.com/devidw/obsidian-to-hugo) for making this super simple.

Nothing fancy; start with `o_to_h.py` to search through your vault for all files where a `draft` property 
is set to `true`. Edit the files as you need. My Hugo configuration doesn't take the photo files the way OtH outputs 
them, so I usually have to edit those.

Then after all edits, call main and input the directory you want to reset to `draft: false` in my Hugo and Vault 
directories. Then publish 👍.