# File Formats

To most operating systems (Windows, OSX), the last three characters of a file after the period are the file extension. For example, notes.txt would be considered a text file because the extension is .txt. Most personal computers today identify files by the extention. .txt is text file, .doc is a Word Document, .xls is an Excel spreadsheet.

However, file extensions are not the sole way to identify the type of a file. Files have certain leading bytes called *file headers* which allow programs to identify what kind of file they are and process it accordingly.

The Linux operating system uses file headers to identify files. So for example if you have a PNG image and rename the file extension to .txt, Linux can still identify the file as a PNG file. This is because the first four bytes of the file (the header) is `89 50 4e 47`. This translates to \x89PNG. Using this header Linux knows that this is still a PNG file even if the extension is txt.