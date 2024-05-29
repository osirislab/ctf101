# File Formats

File Extensions are not the sole way to identify the type of a file, files have certain leading bytes called *file signatures* which allow programs to parse the data in a consistent manner. Files can also contain additional "hidden" data called *metadata* which can be useful in finding out information about the context of a file's data.

## File Signatures

**File signatures** (also known as File Magic Numbers) are bytes within a file used to identify the format of the file. Generally they’re 2-4 bytes long, found at the beginning of a file.

### What is it used for?

Files can sometimes come without an extension, or with incorrect ones. We use file signature analysis to identify the format (file type) of the file. Programs need to know the file type in order to open it properly. It's useful to analyze the file type before any forensics software.

### How do you find the file signature?

You need to be able to look at the binary data that constitutes the file you’re examining. To do this, you’ll use a hexadecimal editor. Once you find the file signature, you can check it against file signature repositories [such as Gary Kessler’s](http://www.garykessler.net/library/file_sigs.html).

!!! Example

    ![File A](images/file-a.jpg)

    The file above, when opened in a hexadecimal editor like `xxd` or `hexdump`, begins with the bytes `FFD8FFE0 00104A46 494600` or in ASCII `ˇÿˇ‡  JFIF` where `\x00` and `\x10` lack symbols. 

    ![Example A](images/xxd.gif)

    Searching in [Gary Kessler’s](http://www.garykessler.net/library/file_sigs.html) database shows that this file signature belongs to a `JPEG/JFIF graphics file`. You can also use the file utility in Linux to determine the file type!

    ```bash
    ▲ ~/examples file file-a.jpg
    file-a.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, comment: "CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), quality = 90", baseline, precision 8, 1024x576, components 3
    ```
